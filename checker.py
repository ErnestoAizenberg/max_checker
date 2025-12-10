import asyncio
import os
from typing import Optional

from dotenv import load_dotenv
import sigmax

load_dotenv()

ACCESS_TOKEN: Optional[str] = os.getenv('ACCESS_TOKEN')

async def main(access_token: str):
    client = sigmax.Client()

    await client.login_with_token(access_token)
    
    try:
        user = await client.get_user_by_phone('+78005553535')
        print(user.name)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if ACCESS_TOKEN:
    print(ACCESS_TOKEN[:3])
    asyncio.run(main(access_token=ACCESS_TOKEN))
else:
    raise ValueError('Set up the ACCESS_TOKEN first')