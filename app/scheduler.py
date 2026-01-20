import schedule
import time
import logging
import os
from pathlib import Path
from datetime import datetime

# Создание директории логов
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Логирование в файл и stdout (для Docker logs)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # stdout для docker logs
        logging.FileHandler(log_dir / 'scheduler.log')  # файл
    ]
)
logger = logging.getLogger(__name__)


def my_task():
    """ВАША ФУНКЦИЯ-ЗАГЛУШКА. Замените содержимое на реальную логику."""
    try:
        logger.info("🚀 Задача запущена!")
        # Пример: здесь API-вызов, обработка данных, GIS-задачи и т.д.
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Время выполнения: {current_time}")
        # raise ValueError("Тест ошибки")  # Раскомментируйте для теста устойчивости
        logger.info("✅ Задача выполнена успешно!")
    except Exception as e:
        logger.error(f"❌ Ошибка в задаче: {e}", exc_info=True)
        # Продолжаем работу несмотря на ошибку


# Планировщик
time_step = 2 # seconds
time_sleep = 2 # seconds
schedule.every(time_step).seconds.do(my_task)


def main():
    logger.info("🔄 Планировщик запущен. Первая задача через 30 мин.")
    while True:
        try:
            schedule.run_pending()
            time.sleep(time_sleep)  # Эффективная проверка (низкая нагрузка CPU)
        except KeyboardInterrupt:
            logger.info("🛑 Остановка по сигналу пользователя.")
            break
        except Exception as e:
            logger.error(f"💥 Критическая ошибка в цикле: {e}", exc_info=True)
            time.sleep(time_sleep)  # Восстановление через минуту


if __name__ == "__main__":
    main()

