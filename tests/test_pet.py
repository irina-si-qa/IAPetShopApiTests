import allure
import requests
BASE_URL = "http://5.181.109.28:9090/api/v3" #путь из сваггера, основной адрес, а далее идет ендпоинт

@allure.feature("Pet")
class TestPet:
    allure.title("Попытка удалить несуществующего питомца")
    def test_delete_nonexistent_pet(self):
        with allure.step("Отправка запроса на удаление несуществующего питомца"):
            response = requests.delete(url=f'{BASE_URL}/pet/9999')
        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, "Код ответа не совпадает с ожидаемым"
        with allure.step("Проверка содержимого body ответа"):
            assert response.text == 'Pet deleted', "Текст ошибки не совпадает с ожидаемым"
