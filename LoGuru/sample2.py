from loguru import logger
import sys # sys нужен для sys.stderr

# Удаляем стандартный обработчик...
logger.remove()
# ...и добавляем новый с уровнем DEBUG.
# ВНИМАНИЕ: это также сбросит формат вывода к самому простому.
# О том, как настроить свой красивый формат, мы поговорим в Части 3.
logger.add(sys.stderr, level="DEBUG")

logger.debug("Теперь это сообщение будет видно!")
logger.info("И это, конечно, тоже.")