import unittest
import grsu

_faculties_list = [{'id': '3952', 'title': 'Военный факультет'}, {'id': '4907', 'title': 'Инженерно-строительный факультет'},
    {'id': '3601', 'title': 'Институт повышения квалификации и переподготовки кадров'},
    {'id': '11', 'title': 'Педагогический факультет'}, {'id': '5017', 'title': 'Учебный центр «Школа точных наук»'},
    {'id': '1', 'title': 'Учреждение'}, {'id': '6', 'title': 'Факультет биологии и экологии'},
    {'id': '5555', 'title': 'Факультет довузовской подготовки'}, {'id': '4908', 'title': 'Факультет инновационных технологий машиностроения'},
    {'id': '4217', 'title': 'Факультет искусств и дизайна'}, {'id': '5211', 'title': 'Факультет истории, коммуникации и туризма'},
    {'id': '3', 'title': 'Факультет математики и информатики'}, {'id': '2280', 'title': 'Факультет психологии'},
    {'id': '2', 'title': 'Факультет физической культуры'}, {'id': '30', 'title': 'Факультет экономики и управления'},
    {'id': '4673', 'title': 'Физико-технический факультет'}, {'id': '8', 'title': 'Филологический факультет'},
    {'id': '10', 'title': 'Юридический факультет'}]

_math_fac_2nd_course_list = [{'id': '6088', 'title': 'МДП-ВМС-161'}, {'id': '6089', 'title': 'МДП-ВМС-162'},
                   {'id': '5033', 'title': 'СДП-КБ-161'}, {'id': '5034', 'title': 'СДП-МАТ(НПД)-161'},
                   {'id': '5145', 'title': 'СДП-ПМ-161'}, {'id': '5146', 'title': 'СДП-ПМ-162'},
                   {'id': '5147', 'title': 'СДП-ПОИТ-161'}, {'id': '5148', 'title': 'СДП-ПОИТ-162'},
                   {'id': '5149', 'title': 'СДП-ПОИТ-163'}, {'id': '5035', 'title': 'СДП-УИР-161'}]

lesson_json_example = {'timeStart': '16:40', 'timeEnd': '18:00',
 'teacher': {'id': '39010', 'fullname': 'Богурин Александр Анатольевич', 'post': 'Старший преподаватель'},
 'type': 'практ. зан.', 'title': 'Физическая культура', 'address': 'Захарова, 32', 'room': 'Спортивный комплекс',
 'subgroup': {'id': '7549', 'title': 'СДР-УН-170.6.1003'}}


class GrSURequestsTest(unittest.TestCase):

    def test_faculties_list(self):
        requested_data = grsu.get_faculties_list()
        self.assertEqual(requested_data,
                         _faculties_list)

    def test_groups_list(self):
        requested_data = grsu.get_groups_list(3, 2)
        self.assertEqual(requested_data, _math_fac_2nd_course_list)


if __name__ == '__main__':
    unittest.main()
