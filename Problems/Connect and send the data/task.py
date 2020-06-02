def submit_data(data, client, address):
    client.connect(address)
    message = data.encode()
    client.send(message)
    client.close()