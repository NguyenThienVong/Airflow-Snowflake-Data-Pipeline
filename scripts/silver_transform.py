import json
import pandas as pd
from pathlib import Path

def run_silver_transform(**context):

    execution_date = context["ds_nodash"]

    bronze_file = context["ti"].xcom_pull(key="bronze_file",
                                          task_ids = "bronze_ingest",)

    if not bronze_file:
        raise ValueError("Bronze file path not found in Xcom")

    silver_path = Path("/opt/airflow/data/silver")
    silver_path.mkdir(parents=True, exist_ok=True)

    with open(bronze_file) as f:
        raw = json.load(f)

    df_raw = pd.DataFrame(raw["states"])

    df_raw.columns = [
        "icao24", "callsign", "origin_country", "time_position", "last_contact",
        "longitude", "latitude", "baro_altitude", "on_ground", "velocity", "true_track",
        "vertical_rate", "sensors", "geo_altitude", "squawk", "spi", "position_source"
    ]

    df = df_raw[
        [
            "icao24",
            "origin_country",
            "velocity",
            "on_ground"
        ]
    ].copy()
    # 8. Làm sạch mã máy bay
    df["icao24"] = (
        df["icao24"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # 9. Làm sạch tên quốc gia
    df["origin_country"] = (
        df["origin_country"]
        .astype("string")
        .str.strip()
    )

    # 10. Chuyển velocity về kiểu số
    df["velocity"] = pd.to_numeric(
        df["velocity"],
        errors="coerce",
    )

    # 11. Chuẩn hóa on_ground
    df["on_ground"] = df["on_ground"].fillna(False)

    # 12. Loại bỏ bản ghi thiếu dữ liệu quan trọng
    df = df.dropna(
        subset=[
            "icao24",
            "origin_country",
            "velocity",
        ]
    )

    # 13. Chỉ giữ velocity hợp lệ
    df = df[df["velocity"] >= 0]

    # 14. Loại bỏ bản ghi trùng mã máy bay
    df = df.drop_duplicates(
        subset=["icao24"],
        keep="last",
    )

    # 15. Tạo đường dẫn file Silver
    output_file = (
        silver_path
        / f"flights_silver_{execution_date}.csv"
    )

    # 16. Lưu dữ liệu đã làm sạch
    df.to_csv(
        output_file,
        index=False,
    )

    output_file = silver_path / f"flights_silver{execution_date}.csv"
    df.to_csv(output_file, index = False)

    context["ti"].xcom_push(
        key = "silver_file",
        value=str(output_file)
    )

    print()

    