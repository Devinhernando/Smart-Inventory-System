import pytest
from app import app
import service as service

@pytest.fixture
def client():
    service.reset_data()
    with app.test_client() as client:
        yield client

# HOME
def test_home(client):
    res = client.get('/')
    assert res.status_code == 200

# CREATE
def test_create_success(client):
    res = client.post('/items', json={"name":"Laptop","stock":10,"price":100})
    assert res.status_code == 201

def test_create_no_name(client):
    res = client.post('/items', json={"stock":10,"price":100})
    assert res.status_code == 400

def test_create_negative_stock(client):
    res = client.post('/items', json={"name":"A","stock":-1,"price":100})
    assert res.status_code == 400

def test_create_invalid_price(client):
    res = client.post('/items', json={"name":"A","stock":10,"price":0})
    assert res.status_code == 400

# GET
def test_get_items_empty(client):
    res = client.get('/items')
    assert res.json == []

def test_get_items_with_data(client):
    client.post('/items', json={"name":"Laptop","stock":10,"price":100})
    res = client.get('/items')
    assert len(res.json) == 1

# UPDATE
def test_update_success(client):
    client.post('/items', json={"name":"A","stock":10,"price":100})
    res = client.put('/items/1', json={"stock":20})
    assert res.status_code == 200

def test_update_not_found(client):
    res = client.put('/items/999', json={"stock":10})
    assert res.status_code == 404

def test_update_invalid_stock(client):
    client.post('/items', json={"name":"A","stock":10,"price":100})
    res = client.put('/items/1', json={"stock":-5})
    assert res.status_code == 400

# DELETE
def test_delete_success(client):
    client.post('/items', json={"name":"A","stock":10,"price":100})
    res = client.delete('/items/1')
    assert res.status_code == 200

def test_delete_not_found(client):
    res = client.delete('/items/999')
    assert res.status_code == 404