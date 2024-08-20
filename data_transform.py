if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[data['passenger_count'] > 0]
    data = data[data['trip_distance'] > 0]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.strftime('%Y-%m-%d')
    data.columns = data.columns.str.lower()

    # Asegurarte de que todos los vendor_id sean valores válidos
    assert data['vendorid'].isin([1, 2]).all(), "Hay valores no válidos en vendor_id"

    # Asegurarte de que passenger_count sea mayor que 0
    assert (data['passenger_count'] > 0).all(), "Hay filas con passenger_count menor o igual a 0"

    # Asegurarte de que trip_distance sea mayor que 0
    assert (data['trip_distance'] > 0).all(), "Hay filas con trip_distance menor o igual a 0"

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
