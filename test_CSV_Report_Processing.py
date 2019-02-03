import pytest
from csv_report_processing import (crt_changing,
                                   get_alpha_3_code,
                                   agregated_data,
                                   save_result_to_file,
                                   csv_extension,
                                   add_impression_click)


@pytest.mark.parametrize('ctr, percentage, row_number, expected', [
    ('432', '6.50%', 1, 28),
    (543, 1.2, 2, 7),
    ('pas', '12eas', 3, None)
])
def test_crt_changing_csv(ctr, percentage, row_number, expected, ):
    total = crt_changing(ctr, percentage, row_number)
    assert total == expected


@pytest.mark.parametrize('city, expected_code', [
    ('Madiana', 'XXX'),
    ('432', 'XXX'),
    ('Lola', 'GIN')
])
def test_alpha_3(city, expected_code):
    result = get_alpha_3_code(city)
    assert result == expected_code or result == expected_code


@pytest.mark.parametrize('city, click, date, impressions, results, expected_result', [
    ('Mandiana', 3, '2019-01-21', 883, {'2019-01-21': {'GIN': [[0, 0]]}}, {'2019-01-21': {'GIN': [[883, 3]]}}),
    ('dsadas', 2, '2017-02-22', 300, {'2017-02-22': {'XXX': [[200, 6]]}}, {'2017-02-22': {'XXX': [[500, 8]]}}),
    ('Mandiana', 3, '2019-01-21', 883, {'2017-02-22': {'XXX': [[500, 8]]}, '2019-01-21': {'GIN': [[0, 0]]}},
     {'2017-02-22': {'XXX': [[500, 8]]}, '2019-01-21': {'GIN': [[883, 3]]}})
])
def test_add_impression_click(city, click, date, impressions, results, expected_result):
    result = add_impression_click(city, click, date, impressions, results)
    assert result == expected_result


@pytest.mark.parametrize('filename, expected_result', [
    ('file.csv', True),
    ('file.txt', False)
])
def test_csv_extension(filename, expected_result):
    result = csv_extension(filename)
    assert result == expected_result


@pytest.mark.parametrize('file_name, expected_result', [
    ('data_to_change.csv', {'2019-01-21':
                      {'AFG': [['919', 6]],
                       'GIN': [[959, 4]]},
                  '2019-01-22':
                      {'CZE': [['139', 1]],
                       'GIN': [[1251, 12]]},
                  '2019-01-23':
                      {'GIN': [[593, 2]],
                       'XXX': [['777', 2]]},
                  '2019-01-24':
                      {'CZE': [['620', 1]],
                       'XXX': [[1668, 12]]}}
     ),
    ('fewsw.txt', {}),
    ('csv2.txt', {})
])
def test_agregated_date(file_name, expected_result):
    result = agregated_data(file_name)
    assert result == expected_result


@pytest.mark.parametrize('results, expected_result', [
    ({'2019-01-21':
          {'AFG': [['919', 6]],
           'GIN': [[959, 4]]},
      '2019-01-22':
          {'CZE': [['139', 1]],
           'GIN': [[1251, 12]]},
      '2019-01-23':
          {'GIN': [[593, 2]],
           'XXX': [['777', 2]]},
      '2019-01-24':
          {'CZE': [['620', 1]],
           'XXX': [[1668, 12]]}}, True),
    ({}, True)
])
def test_save_result_to_file(results, expected_result):
    result = save_result_to_file(results)
    assert result == expected_result