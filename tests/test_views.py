"""
Test code for pytest
"""
# test_views.py

def test_index_ok(client):
    """ So far this only tests for a 200 response """
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
