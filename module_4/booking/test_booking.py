from module_4.booking.constant.constant import BASE_URL


class Test_create_booking():

    def test_create_booking(self, booking_data, auth_session, booking_id):

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронирование не найдено"
        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

class Test_put_booking():

    def test_put_booking(self, booking_data, booking_data_2, auth_session, booking_id):
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200


        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data_2)
        assert put_booking.status_code == 200, "Не удалось обновить данные"
        put_booking_response = put_booking.json()
        assert put_booking_response ['firstname'] == booking_data_2['firstname']
        assert put_booking_response  == booking_data_2

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"


class Test_patch_booking():

    def test_patch_booking(self, booking_data,booking_data_3, auth_session, booking_id):
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        patch_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_data_3)
        assert patch_booking.status_code == 200, "Букинг не обновлен"
        patch_booking_response = patch_booking.json()
        assert patch_booking_response['firstname'] == booking_data_3['firstname'], "Имя не совпадает с обновленным"
        assert patch_booking_response['lastname'] == booking_data_3['lastname'], "Фамилия не совпадает с обновленной"
        assert patch_booking_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной до обновления"
        assert patch_booking_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

class Test_get_booking():

    def test_get_booking(self,auth_session):
        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert get_booking.status_code == 200


