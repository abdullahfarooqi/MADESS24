import pytest
import pandas as pd
from unittest.mock import patch
import sqlite3
import io
from data_processing import read_clean_save_data, url_ozone, url_no2


@pytest.fixture
def mock_csv_data():
    data = '''Measure value;Station code;Station setting;Station type;Date
              10;;Urban;;2024-01-01
              20;;Urban;;2024-01-02
              -;;Urban;;2024-01-03'''
    return data


@pytest.fixture
def setup_database():
    # Create a new SQLite database for testing
    conn = sqlite3.connect('test_project.sqlite')
    yield conn
    conn.close()


@patch('pandas.read_csv')
def test_read_clean_save_data(mock_read_csv, mock_csv_data, setup_database):
    mock_read_csv.return_value = pd.read_csv(io.StringIO(mock_csv_data), sep=';')

    conn = setup_database

    read_clean_save_data(url_ozone, 'Ozone', conn)
    read_clean_save_data(url_no2, 'NO2', conn)

    cursor = conn.cursor()

    # Check if tables are created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Ozone'")
    result = cursor.fetchone()
    print("Ozone table fetch result:", result)
    assert result is not None

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='NO2'")
    result = cursor.fetchone()
    print("NO2 table fetch result:", result)
    assert result is not None

    # Check if data is correctly inserted
    cursor.execute("SELECT * FROM Ozone")
    rows = cursor.fetchall()
    print("Ozone table rows:", rows)
    assert len(rows) == 2  # Should be 2 rows since one row has '-' which is filtered out

    cursor.execute("SELECT * FROM NO2")
    rows = cursor.fetchall()
    print("NO2 table rows:", rows)
    assert len(rows) == 2  # Should be 2 rows since one row has '-' which is filtered out
