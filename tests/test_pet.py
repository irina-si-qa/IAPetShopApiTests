import allure
import requests
BASE_URL = "http://5.181.109.28:9090/api/v3" #путь из сваггера, основной адрес, а далее идет ендпоинт
#урок 1
@allure.feature("Pet")
class TestPet:
    @allure.title("Попытка удалить несуществующего питомца")
    def test_delete_nonexistent_pet(self):
        with allure.step("Отправка запроса на удаление несуществующего питомца"):
            response = requests.delete(url=f'{BASE_URL}/pet/9999')
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, "Код ответа не совпадает с ожидаемым"
        with allure.step("Проверка содержимого body ответа"):
            assert response.text == 'Pet deleted', "Текст ошибки не совпадает с ожидаемым"
#урок 2
    @allure.title("Попытка обновить несуществующего питомца")
    def test_update_nonexistent_pet(self):
        with allure.step("Отправка запроса на удаление несуществующего питомца"):
            payload = {"id": 9999,
                       "name": "Non-existent Pet",
                       "status": "available"
                       }
            response = requests.put(url=f'{BASE_URL}/pet', json=payload)
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 404, "Код ответа не совпадает с ожидаемым"
        with allure.step("Проверка текста ответа"):
            assert response.text == "Pet not found", "Текст ошибки не совпадает с ожидаемым"
#домашка к уроку 2
    @allure.title("Попытка получить информацию о несуществующем питомце")
    def test_get_info_about_nonexisting_pet(self):
        with allure.step("Отправка запроса о получении информации о несуществующем питомце"):
            response = requests.get(url=f'{BASE_URL}/pet/9999')
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 404, "Код ответа не совпадает с ожидаемым"
        with allure.step("Проверка текста ответа"):
            assert response.text == "Pet not found", "Текст ответа не совпадает с ожидаемым"