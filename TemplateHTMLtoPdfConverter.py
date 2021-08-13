# -*- coding: utf-8 -*-
import os
import pdfkit
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

class Input_info:
    def date_preparatin(self):
        mounth_str = {
            '1':'січня',
            '2':'лютого',
            '3':'березня',
            '4':'квітня',
            '5':'травня',
            '6':'червня',
            '7':'липня',
            '8':'серпня',
            '9':'вересня',
            '10':'жовтня',
            '11':'листопада',
            '12':'грудня',
        }
        day = str(datetime.now().day)
        month = mounth_str.get(str(datetime.now().month))
        year = str(datetime.now().year)
        minut = str(datetime.now().minute)
        result_date = year+'_'+day+month+'_id'+minut
        return  day, month, year, result_date


    def input_templ_data(self):
        value_template_variables = {}
        print('_' * 30,'СТОРОНА Заставодавець','_' * 30)
        value_template_variables['company_1_name'] = input('Назва компанії 1: ')
        value_template_variables['name_person_1'] = input('Ім"я представника компанії 1: ')
        value_template_variables['position_person_1'] = input('Посада представника компанії 1: ')
        value_template_variables['document_1'] = input('Документ, що посвідчує повноваження: ')
        print('_' * 30,'СТОРОНА Заставодержатель','_'*30)
        value_template_variables['company_2_name'] = input('Назва компанії 2: ')
        value_template_variables['name_person_2'] = input('Ім"я представника компанії 2: ')
        value_template_variables['position_person_2'] = input('Посада представника компанії 1: ')
        value_template_variables['document_2'] = input('Документ, що посвідчує повноваження: ')
        print('_' * 100)
        day, month, year, _ = self.date_preparatin()
        print('Залишаю поточну дату:', end=' ')
        print(day, end=' ')
        print(month, end=' ')
        print(year)
        print('_' * 100)
        value_template_variables['day'] = day
        value_template_variables['month'] = month
        value_template_variables['year'] = year
        return value_template_variables


class Template_executor:
    def __init__(self, template_filename, value_template_variables):
        self.template_filename = template_filename
        self.value_template_variables = value_template_variables

    def template_render(self):
        env = Environment(loader=FileSystemLoader("."))
        templ = env.get_template(self.template_filename)
        return templ.render(self.value_template_variables)


class HTMLtoPDFconvertor:
    def __init__(self, **kwargs):
        self.input_html, self.output_filename = kwargs.values()

    def HTMLtoPDFconvertor(self):
        result = pdfkit.from_string(self.input_html, self.output_filename)
        return result


if __name__ == '__main__':
    command_ps = os.system('clear')
    value_template_variables = Input_info().input_templ_data()
    input_filename = 'dogivir.html'
    input_html = Template_executor(input_filename, value_template_variables).template_render()
    output_filename = f'{value_template_variables.get("company_1_name")}_{Input_info().date_preparatin()[3]}.pdf'
    filename = {
        'input_html': input_html,
        'output_filename': output_filename
    }
    if HTMLtoPDFconvertor(**filename).HTMLtoPDFconvertor():
        print('_' * 100)
        print(f'Документ {filename.get("output_filename")}, успішно створено')
        print('_' * 100)