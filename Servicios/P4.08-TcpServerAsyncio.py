import asyncio

async def handle_echo(reader, writer):
  data = await reader.readline()
  mensaje = data.decode()
  addr = writer.get_extra_info('peername')

  print(f"Recibido {mensaje!r} de {addr!r}")

  print(f"Enviado: {mensaje!r}")
  writer.write(data)
  await writer.drain()

  print("Cliente cerrado")
  writer.close()

async def main():
  server = await asyncio.start_server(
    handle_echo, '127.0.0.1', 2000)

  addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
  print(f'Servidor en {addrs}')

  async with server:
    await server.serve_forever()

asyncio.run(main())