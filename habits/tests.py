from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""

        # Создание пользователя для тестирования
        self.user = User.objects.create(telegram='Doctor_Lynch_',
                                        email='test@test.ru',
                                        is_staff=True,
                                        is_superuser=True,
                                        is_active=True)

        self.user.set_password('12345')  # Устанавливаем пароль
        self.user.save()  # Сохраняем изменения пользователя в базе данных

        # Создание привычки для тестирования
        self.habit = Habit.objects.create(
            user=self.user,
            place="Лавочка у дома",
            time="11:30",
            action="Выпивать алкоголь",
            execution_time=25,
        )

        # Запрос токена для авторизации
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': '12345'})

        self.access_token = response.data.get('access')  # Токен для авторизации

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Авторизация пользователя

    def test_create_habit(self):
        """Тестирование создания привычки"""

        # Данные для создания привычки
        data = {
            "user": 1,
            "place": "Лавочка у дома",
            "time": "11:30",
            "action": "Выпивать алкоголь",
            "execution_time": 25
        }

        response = self.client.post(reverse('app_habit:habit_create'), data=data)  # Отправка запроса

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

        self.assertEqual(Habit.objects.all().count(), 2)  # Проверка наличия в базе данных новой записи

    def test_public_list_habit(self):
        """Тестирование списка просмотра публичных привычек"""

        response = self.client.get(reverse('app_habit:habits_is_public'))  # Запрос на получение списка привычек

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(), [])

    def test_list_habit(self):
        """Тестирование списка просмотра личных привычек"""

        response = self.client.get(reverse('app_habit:habits'))  # Запрос на получение списка личных привычек

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос

        # Проверка корректности выводимых данных
        self.assertEqual(response.json()['results'],
                         [{
                             "id": 1,
                             "place": "Лавочка у дома",
                             "time": "11:30:00",
                             "action": "Выпивать алкоголь",
                             "is_pleasant": False,
                             "periodicity": 1,
                             "reward": None,
                             "execution_time": 25,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         }])

    def test_update_habit(self):
        """Тестирование редактирования привычки"""

        # Данные для обновления привычки
        data = {
            "user": 1,
            "place": "Университет",
            "time": "11:00",
            "action": "Клеить жвачку под парту",
            "execution_time": 119
        }

        # Запрос на обновление урока
        response = self.client.put(reverse('app_habit:habit_update', args=[self.habit.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "place": "Университет",
                             "time": "11:00:00",
                             "action": "Клеить жвачку под парту",
                             "is_pleasant": False,
                             "periodicity": 1,
                             "reward": None,
                             "execution_time": 119,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         })

    def test_get_habit_by_id(self):
        """Тестирование получения привычки по id"""

        # Запрос на получение привычки по id
        response = self.client.get(reverse('app_habit:habit', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа

        # Проверка корректности выводимых данных
        self.assertEqual(response.json(),
                         {
                             "id": 1,
                             "place": "Лавочка у дома",
                             "time": "11:30:00",
                             "action": "Выпивать алкоголь",
                             "is_pleasant": False,
                             "periodicity": 1,
                             "reward": None,
                             "execution_time": 25,
                             "is_public": False,
                             "user": 1,
                             "related_habit": None
                         })

    def test_destroy_habit(self):
        """Тестирование удаления привычки"""

        # Запрос на удаление урока
        response = self.client.delete(reverse('app_habit:habit_delete', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        self.assertEqual(Habit.objects.all().count(), 0)  # Проверка количества БД