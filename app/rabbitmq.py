# /app/rabbitmq.py

import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage

from app.settings import settings
from app.services.character_service import CharacterService
from app.repositories.character_repo import CharacterRepo
from app.models.character import Character


async def process_created_character(msg: IncomingMessage):
  try:
      data = json.loads(msg.body.decode())
      character = Character(
          id=data['id'],
          name=data['name'],
          class_name=data['class_name'],
          level=data['level'],
          experience=data['experience'],
          strength=data['strength'],
          agility=data['agility'],
          intelligence=data['intelligence'],
          luck=data['luck']
      )
      repo = CharacterRepo()
      created_character = repo.create_character(character)
      await msg.ack()
      return created_character
  except:
      traceback.print_exc()
      await msg.ack()

async def process_get_character(msg: IncomingMessage):
  try:
      repo = CharacterRepo()
      characters = repo.get_characters()
      await msg.ack()
      return characters
  except:
      await msg.ack()



async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    order_created_queue = await channel.declare_queue('created_character_queue', durable=True)
    order_paid_queue = await channel.declare_queue('get_characters_queue', durable=True)

    await order_created_queue.consume(process_created_character)
    await order_paid_queue.consume(process_get_character)
    print('Started RabbitMQ consuming...')

    return connection
