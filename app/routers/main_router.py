from fastapi import APIRouter

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger_printer = logging.getLogger(__name__)

main_router = APIRouter()

@main_router.get("/login")
async def login():
    logger_printer.info("manfredo godofredo")
    return {}