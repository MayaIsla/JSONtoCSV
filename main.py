import json
import pandas
import pandas as pd


def read_json(filename: str) -> dict:
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data


def create_dataframe(data: list) -> pandas.DataFrame:

    dataframe = pandas.DataFrame()

    # Looping through each record
    for d in data:
        # Normalize the column levels
        record = pandas.json_normalize(d)

        dataframe = dataframe.append(record, ignore_index=True)

    return dataframe


def main():
    # Read JSON file
    data = read_json(filename="input.json")

    dataframe = create_dataframe(data=data['data'])

    print("Normalized Columns:", dataframe.columns.to_list())
#Change column names manually in CSV
    dataframe.rename(columns={
        "attributes.userfirstname": "userfirstname"
    }, inplace=True)

    print("Renamed Columns:", dataframe.columns.to_list())

    # Convert dataframe to CSV
    dataframe.to_csv("output.csv", index=False)


if __name__ == '__main__':
    main()
