from influxdb import InfluxDBClient

# GitHub Secretsから必要な情報を取得
INFLUXDB_URL = "INFLUXDB_URL"
INFLUXDB_USERNAME = "INFLUXDB_USERNAME"
INFLUXDB_PASSWORD = "INFLUXDB_PASSWORD"
DATABASE_NAME = "DATABASE_NAME"

def connect_to_influxdb():
    client = InfluxDBClient(INFLUXDB_URL, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD)
    client.switch_database(DATABASE_NAME)
    return client

def write_data_to_influxdb(client, measurement, fields):
    json_body = [
        {
            "measurement": measurement,
            "fields": fields
        }
    ]
    client.write_points(json_body)

def read_data_from_influxdb(client, query):
    result = client.query(query)
    return result

# メイン処理
def main():
    # InfluxDBに接続
    influxdb_client = connect_to_influxdb()

    # データを書き込む例
    write_data_to_influxdb(influxdb_client, "example_measurement", {"value": 42})

    # データを読み取る例
    result = read_data_from_influxdb(influxdb_client, "SELECT * FROM example_measurement")
    print(result)

if __name__ == "__main__":
    main()
