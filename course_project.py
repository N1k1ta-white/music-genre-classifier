# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: ml_practice
#     language: python
#     name: python3
# ---

# %% [markdown] cell_id="d2072d08be074b5eac232f64efc9ced6" deepnote_app_block_group_id deepnote_app_block_order=0 deepnote_app_block_visible=true deepnote_block_group="725a1be99d2e40c798dc6da65f026532" deepnote_cell_type="text-cell-h1" deepnote_sorting_key="0" deepnote_source="\u0414\u043e\u043c\u0430\u0448\u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 3" formattedRanges=[] id="0tygKv9zYB7N"
# # Курсова работа

# %% [markdown] cell_id="caecadd6dcbf4e8eba85cb9d25c300e4" deepnote_block_group="78894b0f566243b0b1f1dd1a00af9a58" deepnote_cell_type="markdown" deepnote_sorting_key="1" deepnote_source="## \u0415\u043a\u0438\u043f\n\n- **\u041c\u0438\u043a\u0438\u0442\u0430 \u0411\u0438\u043b\u0438\u0439** \u2013 \u0424\u0430\u043a\u0443\u043b\u0442\u0435\u0442\u0435\u043d \u043d\u043e\u043c\u0435\u0440: **9MI8000022**  \n  \u0411\u0430\u043a\u0430\u043b\u0430\u0432\u044a\u0440\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0430: **\u201e\u0421\u043e\u0444\u0442\u0443\u0435\u0440\u043d\u043e \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0441\u0442\u0432\u043e\u201c**\n\n- **\u0420\u0430\u044f \u0413\u0440\u0438\u0433\u043e\u0440\u043e\u0432\u0430** \u2013 \u0424\u0430\u043a\u0443\u043b\u0442\u0435\u0442\u0435\u043d \u043d\u043e\u043c\u0435\u0440: **5MI0600167**  \n  \u0411\u0430\u043a\u0430\u043b\u0430\u0432\u044a\u0440\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0430: **\u201e\u0421\u043e\u0444\u0442\u0443\u0435\u0440\u043d\u043e \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0441\u0442\u0432\u043e\u201c**\n" id="PuUfDwsCYB7P"
# ## Екип
#
# - **Микита Билий** – Факултетен номер: **9MI8000022**  
#   Бакалавърска програма: **„Софтуерно инженерство“**
#
# - **Рая Григорова** – Факултетен номер: **5MI0600167**  
#   Бакалавърска програма: **„Софтуерно инженерство“**
#

# %% [markdown] cell_id="532964dca58e4ae3b2ff53919cf7db39" deepnote_block_group="38f764e5cef64e239bc5099c14f47c72" deepnote_cell_type="markdown" deepnote_sorting_key="2" deepnote_source="## \u0422\u0438\u043f \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430\n- **C. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u0430 \u0442\u0435\u043c\u0430** \u2013 \u043f\u0440\u043e\u0435\u043a\u0442 \u0432\u044a\u0440\u0445\u0443 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e \u0434\u043e\u0441\u0442\u044a\u043f\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (Kaggle), \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d \u0432 Python (Jupyter Notebook), \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0449 \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f.\n\n## \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 (\u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442)\n- **\u201e\u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0447\u0440\u0435\u0437 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u201c**  \n  **\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442:** \u041c\u0430\u0448\u0438\u043d\u043d\u043e \u0441\u0430\u043c\u043e\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u0432\u044a\u0440\u0445\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f)\n" id="WfraRKDFYB7P"
# ## Тип на проекта
# - **C. Собствена тема** – проект върху публично достъпни данни (Kaggle), реализиран в Python (Jupyter Notebook), включващ задачи по класификация и клъстеризация.
#
# ## Название на проекта (предметна област)
# - **„Класификация на музикални жанрове и групиране на песни по настроение чрез таблични аудио характеристики“**  
#   **Предметна област:** Машинно самообучение върху таблични данни (класификация и клъстеризация)
#

# %% [markdown] cell_id="fac6c5cbb4d447d1b7ed0f7d55451df3" deepnote_block_group="499ce469ca4c40b78030820b83a03fd1" deepnote_cell_type="markdown" deepnote_sorting_key="3" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430\n\n\u0426\u0435\u043b\u0442\u0430 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0435 \u0434\u0430 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430 \u0434\u043e\u043a\u043e\u043b\u043a\u043e **\u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438**, \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u043e\u0442 Spotify, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u043e \u0441\u044a\u0434\u044a\u0440\u0436\u0430\u043d\u0438\u0435 \u0447\u0440\u0435\u0437 \u043c\u0435\u0442\u043e\u0434\u0438 \u0437\u0430 \u043c\u0430\u0448\u0438\u043d\u043d\u043e \u0441\u0430\u043c\u043e\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435. \u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u043a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430 \u0434\u0432\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 \u0437\u0430\u0434\u0430\u0447\u0438: **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435** \u0438 **\u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u0435\u043d (mood) \u043f\u0440\u043e\u0444\u0438\u043b**.\n\n\u0412 \u043f\u044a\u0440\u0432\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f, \u043f\u0440\u0438 \u043a\u043e\u044f\u0442\u043e \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u0436\u0430\u043d\u0440\u044a\u0442 \u043d\u0430 \u0434\u0430\u0434\u0435\u043d\u0430 \u043f\u0435\u0441\u0435\u043d \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043a\u0430\u0442\u043e *danceability, energy, acousticness, valence* \u0438 \u0434\u0440\u0443\u0433\u0438. \u0426\u0435\u043b\u0442\u0430 \u0435 \u0434\u0430 \u0441\u0435 \u0441\u0440\u0430\u0432\u043d\u044f\u0442 \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u043a\u043e\u0438 \u043e\u0442 \u0442\u044f\u0445 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0435 \u043f\u0440\u0438 \u0442\u0430\u0437\u0438 \u0437\u0430\u0434\u0430\u0447\u0430.\n\n\u0412\u044a\u0432 \u0432\u0442\u043e\u0440\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0432\u044a\u0440\u0445\u0443 \u0441\u044a\u0449\u0438\u0442\u0435 \u0438\u043b\u0438 \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441 \u0446\u0435\u043b **\u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435**, \u0431\u0435\u0437 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u043e \u0437\u0430\u0434\u0430\u0434\u0435\u043d\u0438 \u0435\u0442\u0438\u043a\u0435\u0442\u0438. \u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0442\u0435 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438 \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0438\u0440\u0430\u043d\u0438 \u0447\u0440\u0435\u0437 \u043e\u0431\u043e\u0431\u0449\u0435\u043d\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 \u043d\u0430 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0438\u0437\u0432\u0435\u0436\u0434\u0430\u043d\u0435 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u0444\u0438\u043b\u0438 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435.\n\n\u041a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430\u043d\u0435\u0442\u043e \u043d\u0430 \u0442\u0435\u0437\u0438 \u0434\u0432\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u043f\u043e-\u043f\u044a\u043b\u043d\u043e \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u2013 \u043a\u0430\u043a\u0442\u043e \u043e\u0442 \u0433\u043b\u0435\u0434\u043d\u0430 \u0442\u043e\u0447\u043a\u0430 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0430 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442, \u0442\u0430\u043a\u0430 \u0438 \u043f\u043e \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u044a\u0442\u0440\u0435\u0448\u043d\u0438\u0442\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0435\u0441\u043d\u0438\u0442\u0435, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0435 \u0443\u043b\u0430\u0432\u044f\u0442 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u0442\u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u0438.\n" id="gscrh20kYB7P"
# ## Кратко описание на проекта
#
# Целта на проекта е да изследва доколко **аудио характеристиките на песни**, предоставени от Spotify, позволяват автоматичен анализ на музикално съдържание чрез методи за машинно самообучение. Проектът комбинира две основни задачи: **класификация на музикални жанрове** и **клъстеризация на песни по емоционален (mood) профил**.
#
# В първата част се разглежда задача по класификация, при която се предсказва жанрът на дадена песен на база числови аудио признаци като *danceability, energy, acousticness, valence* и други. Целта е да се сравнят класически алгоритми за класификация и да се оцени кои от тях се справят най-добре при тази задача.
#
# Във втората част се прилага клъстеризация върху същите или подмножество от аудио характеристики с цел **групиране на песни по настроение**, без използване на предварително зададени етикети. Получените клъстери ще бъдат интерпретирани чрез обобщени стойности на аудио характеристиките, което позволява извеждане на типични емоционални профили на песните.
#
# Комбинирането на тези две задачи позволява по-пълно разглеждане на данните – както от гледна точка на жанрова принадлежност, така и по отношение на вътрешните различия между песните, които не се улавят директно от жанровите етикети.
#
# ## Разпределение на задачите и принос по секции
#
# **Забележка:** Посоченото разпределение на секциите не отразява тяхната относителна сложност или обем на работа, тъй като отделните части на проекта имат различна тежест и изискват различен тип усилия - текстовите секции са по-леки и по-малко времеемки спрямо техническите.
#
# | Секция                                                                   | Автор         |
# | ------------------------------------------------------------------------ | ------------- |
# | Общи текстови описания (исп. данни, библиотеки, алгоритми, заключение    | Рая Григорова |
# | Визуализации и първоначален EDA на данните                               | Микита Билий  |
# | Част 1: Класификационна задача – предсказване на жанр                    | Рая Григорова |
# | Част 2: Кластъризация                                                    | Микита Билий  |
# | Част 3: Обучение и валидиране на модели чрез използване на супер-класове | Рая Григорова и Микита Билий (частично)|
#
#

# %% [markdown] cell_id="3b0ccfb7a06c4dbca5489b429cadbf4d" deepnote_block_group="9ab58838d7cd488288d7b407702290b2" deepnote_cell_type="markdown" deepnote_sorting_key="4" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u0438\n\n\u0412 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e \u0434\u043e\u0441\u0442\u044a\u043f\u0435\u043d \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u043e\u0442 \u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430\u0442\u0430 Kaggle \u2013 **[Spotify Tracks Genre Dataset](https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset)** (`thedevastator/spotify-tracks-genre-dataset`), \u043a\u043e\u0439\u0442\u043e \u0435 \u0438\u0437\u0442\u0435\u0433\u043b\u0435\u043d \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u0432 \u0440\u0430\u0431\u043e\u0442\u043d\u0430\u0442\u0430 \u0441\u0440\u0435\u0434\u0430 \u0447\u0440\u0435\u0437 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430\u0442\u0430 `kagglehub`. \u041d\u0430\u0431\u043e\u0440\u044a\u0442 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u0441\u044a\u0434\u044a\u0440\u0436\u0430 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e\u0434\u0433\u043e\u0442\u0432\u0435\u043d\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u0437\u0430 \u043f\u0435\u0441\u043d\u0438 \u043e\u0442 Spotify \u0438 \u0435 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d \u0437\u0430 \u0430\u043d\u0430\u043b\u0438\u0437 \u0438 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u043d\u0435 \u0432\u044a\u0440\u0445\u0443 \u0432\u0435\u0447\u0435 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438.\n\n\u0414\u0430\u043d\u043d\u0438\u0442\u0435 \u0441\u0430 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u0432 \u0442\u0430\u0431\u043b\u0438\u0447\u0435\u043d \u0444\u043e\u0440\u043c\u0430\u0442 (`CSV` \u0444\u0430\u0439\u043b \u2013 `train.csv`) \u0438 \u0441\u044a\u0434\u044a\u0440\u0436\u0430\u0442 \u043f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u0435\u043b\u043d\u043e **114 000 \u0437\u0430\u043f\u0438\u0441\u0430** \u0441 **20 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0430**, \u043a\u0430\u0442\u043e \u0432\u0441\u0435\u043a\u0438 \u0437\u0430\u043f\u0438\u0441 \u043e\u0442\u0433\u043e\u0432\u0430\u0440\u044f \u043d\u0430 \u0435\u0434\u043d\u0430 \u043f\u0435\u0441\u0435\u043d. \u0427\u0430\u0441\u0442 \u043e\u0442 \u043a\u043e\u043b\u043e\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0432\u0430\u0442 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0438 \u0438 \u043e\u043f\u0438\u0441\u0430\u0442\u0435\u043b\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (\u043d\u0430\u043f\u0440. `track_id`, `artists`, `album_name`, `track_name`), \u0430 \u043e\u0441\u0442\u0430\u043d\u0430\u043b\u0438\u0442\u0435 \u2013 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u043e\u043f\u0438\u0441\u0432\u0430\u0449\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438\u0442\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435.\n\n\u041e\u0441\u043d\u043e\u0432\u043d\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0438 \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0430, \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0442:\n- *danceability*, *energy*, *loudness*, *speechiness*, *acousticness*,\n- *instrumentalness*, *liveness*, *valence*, *tempo*,\n\u043a\u0430\u043a\u0442\u043e \u0438 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u043a\u0430\u0442\u043e \u043f\u0440\u043e\u0434\u044a\u043b\u0436\u0438\u0442\u0435\u043b\u043d\u043e\u0441\u0442 (`duration_ms`), \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442 (`popularity`), \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u043a\u043b\u044e\u0447 \u0438 \u0442\u0430\u043a\u0442.\n\n\u0426\u0435\u043b\u0435\u0432\u0430\u0442\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0437\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0435 \u043a\u043e\u043b\u043e\u043d\u0430\u0442\u0430 **`track_genre`**, \u043a\u043e\u044f\u0442\u043e \u0441\u044a\u0434\u044a\u0440\u0436\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u044f \u0435\u0442\u0438\u043a\u0435\u0442 \u043d\u0430 \u0432\u0441\u044f\u043a\u0430 \u043f\u0435\u0441\u0435\u043d. \u0417\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043f\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u043e\u0432\u0430\u0442\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f." id="-XCsiL-jYB7P"
# ## Кратко описание на използваните данни
#
# В проекта се използва публично достъпен набор от данни от платформата Kaggle – **[Spotify Tracks Genre Dataset](https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset)** (`thedevastator/spotify-tracks-genre-dataset`), който е изтеглен директно в работната среда чрез библиотеката `kagglehub`. Наборът от данни съдържа предварително подготвена информация за песни от Spotify и е предназначен за анализ и моделиране върху вече извлечени аудио характеристики.
#
# Данните са предоставени в табличен формат (`CSV` файл – `train.csv`) и съдържат приблизително **114 000 записа** с **20 атрибута**, като всеки запис отговаря на една песен. Част от колоните представляват идентификационни и описателни данни (напр. `track_id`, `artists`, `album_name`, `track_name`), а останалите – числови характеристики, описващи музикалните свойства на песните.
#
# Основните аудио характеристики, използвани в проекта, включват:
# - *danceability*, *energy*, *loudness*, *speechiness*, *acousticness*,
# - *instrumentalness*, *liveness*, *valence*, *tempo*,
# както и допълнителни параметри като продължителност (`duration_ms`), популярност (`popularity`), музикален ключ и такт.
#
# Целевата променлива за задачата по класификация е колоната **`track_genre`**, която съдържа жанровия етикет на всяка песен. За задачата по клъстеризация се използват само числовите аудио характеристики, без жанровата информация.

# %% [markdown] cell_id="7715c7f0a7a44b228158e00e6ae12887" deepnote_block_group="2bdcbc20d7b04a0d8d1a8c1d06c808f7" deepnote_cell_type="markdown" deepnote_sorting_key="5" deepnote_source="## \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u0435\u043d EDA \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435\n\n\u0412 \u0442\u0430\u0437\u0438 \u0441\u0435\u043a\u0446\u0438\u044f \u0441\u0435 \u043f\u0440\u0430\u0432\u0438 **\u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u043d\u043e \u043e\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438** \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0434\u0430\u043b\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u043e\u0441\u044f\u0442 \u0441\u0438\u0433\u043d\u0430\u043b \u0437\u0430 \u0436\u0430\u043d\u0440\u0430 \u0438 \u0437\u0430 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u043e \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435.\n\n\u041d\u0430 \u0432\u0438\u0441\u043e\u043a\u043e \u043d\u0438\u0432\u043e \u043a\u043e\u0434\u044a\u0442:\n- \u0438\u043d\u0441\u0442\u0430\u043b\u0438\u0440\u0430 \u043d\u0443\u0436\u043d\u0438\u0442\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 (`kagglehub`, `statsmodels`) \u0438 **\u0438\u0437\u0442\u0435\u0433\u043b\u044f** \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430 \u043e\u0442 Kaggle;\n- **\u0437\u0430\u0440\u0435\u0436\u0434\u0430** `train.csv` \u0432 `pandas` DataFrame \u0438 \u043f\u0440\u0430\u0432\u0438 \u0431\u0430\u0437\u043e\u0432\u0430 \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f (\u043f\u0440\u0435\u0433\u043b\u0435\u0434 \u043d\u0430 \u0440\u0435\u0434\u043e\u0432\u0435/\u043a\u043e\u043b\u043e\u043d\u0438, \u0443\u043d\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435);\n- \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0432\u0430 \u0437\u0430 **\u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438**;\n- \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u0430 **\u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f** \u043d\u0430 \u043a\u043b\u044e\u0447\u043e\u0432\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (`danceability`, `energy`, `tempo`) \u0438 \u043d\u0430 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0438 (`explicit`, `mode`, `key`);\n- \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 **\u0432\u0440\u044a\u0437\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435** \u0447\u0440\u0435\u0437 pairplot \u0438 \u043a\u043e\u0440\u0435\u043b\u0430\u0446\u0438\u043e\u043d\u043d\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u0430;\n- \u0441\u0440\u0430\u0432\u043d\u044f\u0432\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 **\u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435** (\u043d\u0430\u043f\u0440. boxplot \u043d\u0430 `energy` \u043f\u043e \u0436\u0430\u043d\u0440, \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 major/minor \u043f\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435);\n- \u043f\u0440\u0430\u0432\u0438 **PCA \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f** \u0437\u0430 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (\u0441\u043b\u0435\u0434 \u0441\u043a\u0430\u043b\u0438\u0440\u0430\u043d\u0435), \u0437\u0430 \u0434\u0430 \u0441\u0435 \u0432\u0438\u0434\u0438 \u0434\u0430\u043b\u0438 \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430 \u0435\u0441\u0442\u0435\u0441\u0442\u0432\u0435\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435;\n- \u043f\u0440\u0430\u0432\u0438 **\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430** \u043a\u043e\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u043e \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 (ANOVA + \u0435\u0444\u0435\u043a\u0442 \u0440\u0430\u0437\u043c\u0435\u0440) \u0438 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (Tukey HSD)." id="zHZQQrZIYB7Q"
# ## Визуализации и първоначален EDA на данните
#
# В тази секция се прави **първоначално опознаване на набора от данни** и проверка дали аудио характеристиките носят сигнал за жанра и за потенциално групиране по настроение.
#
# На високо ниво кодът:
# - инсталира нужните библиотеки (`kagglehub`, `statsmodels`) и **изтегля** датасета от Kaggle;
# - **зарежда** `train.csv` в `pandas` DataFrame и прави базова инспекция (преглед на редове/колони, уникални жанрове);
# - проверява за **липсващи стойности**;
# - визуализира **разпределения** на ключови характеристики (`danceability`, `energy`, `tempo`) и на категориални променливи (`explicit`, `mode`, `key`);
# - разглежда **връзки между признаците** чрез pairplot и корелационна матрица;
# - сравнява признаци **между жанрове** (напр. boxplot на `energy` по жанр, разпределение major/minor по жанрове);
# - прави **PCA проекция** за избрани жанрове (след скалиране), за да се види дали се наблюдава естествено разделяне;
# - прави **статистическа проверка** кои признаци се различават най-силно между жанровете (ANOVA + ефект размер) и допълнителни сравнения между избрани жанрове (Tukey HSD).

# %% cell_id="a7c491d1294547f29ffa80cf055d0d74" deepnote_block_group="a38f6c1009874338a9c986e5827f9f72" deepnote_cell_type="code" deepnote_content_hash="20199392" deepnote_execution_finished_at="2026-01-27T21:47:00.392Z" deepnote_execution_started_at="2026-01-27T21:47:00.138Z" deepnote_sorting_key="6" deepnote_source="# \u041e\u0441\u043d\u043e\u0432\u043d\u0438 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438\nimport numpy as np\nimport pandas as pd\n\n# \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 (EDA/\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442)\nfrom scipy import stats\nfrom statsmodels.stats.multicomp import pairwise_tukeyhsd\n\n# Scikit-learn: preprocessing / dim reduction / split / pipeline\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.decomposition import PCA\nfrom sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler\n\n# Scikit-learn: \u043c\u043e\u0434\u0435\u043b\u0438\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.svm import LinearSVC\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.neural_network import MLPClassifier\n\n# Scikit-learn: \u043c\u0435\u0442\u0440\u0438\u043a\u0438\nfrom sklearn.metrics import (\n    accuracy_score,\n    f1_score,\n    classification_report,\n    confusion_matrix,\n    ConfusionMatrixDisplay\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=254 execution_start=1769550420138 id="adD8JvJvYB7Q" source_hash="20199392"
# Основни библиотеки
import numpy as np
import pandas as pd

# Визуализация
import matplotlib.pyplot as plt
import seaborn as sns

# Статистика (EDA/значимост)
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Scikit-learn: preprocessing / dim reduction / split / pipeline
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler

# Scikit-learn: модели
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import ExtraTreesClassifier, HistGradientBoostingClassifier

# Scikit-learn: метрики
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# %% id="sGlqeUJaB_3h"
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# %% [markdown] id="RmB1z_zaa62Z"
# ### Зареждане на данните
#
# Има два начина да заредите датасета. **Изпълнете само един от двата варианта**:
#
# #### Вариант 1 (в Colab) – качване на `.zip` и разархивиране
# 1. **Качете файла** `spotify-tracks-genre-dataset.zip` **в Colab**, след което го преместете/сложете в папка: **`/content/data/`**
#
#    * Най-лесно: от **Files панела** (ляво) качете zip-а (обикновено отива в `/content/`) и го **преместете** в папката `data` или го **преименувайте**, ако е нужно.
#    * Важно: пътят трябва да е **точно** `/content/data/spotify-tracks-genre-dataset.zip`, за да работи unzip клетката.
# 2. Изпълнете следващите клетки за **разархивиране** и **четене** от `/content/data/` (след unzip очакваме `train.csv` да е в `/content/data/`).
#
#
# #### Вариант 2 (ако имате Kaggle достъп) – `kagglehub`
# Изпълнете клетките с `pip install kagglehub`, `kagglehub.dataset_download(...)` и четене на `train.csv` от кеша.
#
# > Забележка: В настоящия проект има клетки, маркирани като **(в Colab)**, защото авторът няма достъп до Kaggle акаунт и използва upload на zip.

# %% id="xGgnG7l8bCSr"
# (в Colab) Upload на zip файла (ако не сте го качили ръчно през Files панела)
# В Jupyter извън Colab тази клетка може да се пропусне.
try:
    from google.colab import files  # type: ignore
    uploaded = files.upload()
    print("Uploaded:", list(uploaded.keys()))
except Exception as e:
    print("Тази клетка е предназначена за Google Colab. Пропуснете я извън Colab.")
    print("Details:", e)

# %% colab={"base_uri": "https://localhost:8080/"} id="phh4qV0AdItn" outputId="745e1589-c67a-436a-a7d6-4c9eb383d641"
# (в Colab) Разархивиране на dataset zip (очаквано име: spotify-tracks-genre-dataset.zip)
# !mkdir -p /content/data
# !unzip -o /content/data/spotify-tracks-genre-dataset.zip -d /content/data
# !ls -lah /content/data

# %% colab={"base_uri": "https://localhost:8080/"} id="g2kkO0E7d-tV" outputId="cbca769c-2e27-4df2-dbf6-2764009d87d4"
# (в Colab) Четене на train.csv от /content/data и (по желание) семплиране за по-лека работа
df = pd.read_csv("/content/data/train.csv", index_col=0)

# за да не умира RAM на Agglomerative (и после на sub-clusters)
df = df.sample(n=12000, random_state=42).reset_index(drop=True)

df.shape

# %% cell_id="9b33424659a94d278da08c3acf250d86" deepnote_app_block_group_id deepnote_app_block_order=3 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="0604134473cd4f099f9b2422fe12bf12" deepnote_cell_type="code" deepnote_content_hash="ed7bd955" deepnote_execution_finished_at="2026-01-27T21:46:48.693Z" deepnote_execution_started_at="2026-01-27T21:46:40.377Z" deepnote_sorting_key="7" deepnote_source="!pip install kagglehub statsmodels" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=8316 execution_start=1769550400377 id="JYk0Dj1TYB7R" outputId="018f019a-8fd5-47d6-ae79-4591239e04d1" source_hash="ed7bd955"
# (Алтернатива) Ако имате Kaggle достъп: инсталиране на kagglehub
# !pip install kagglehub statsmodels

# %% cell_id="f38564bca7294c72ae304eb1b933c5c1" deepnote_app_block_group_id deepnote_app_block_order=4 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="da14cae1b4ce404abfc1a9afd1e53b16" deepnote_cell_type="code" deepnote_content_hash="7b09edc6" deepnote_execution_finished_at="2026-01-27T21:47:06.292Z" deepnote_execution_started_at="2026-01-27T21:47:05.171Z" deepnote_sorting_key="8" deepnote_source="import kagglehub\n\n# Download latest version\npath = kagglehub.dataset_download(\"thedevastator/spotify-tracks-genre-dataset\")\n\nprint(\"Path to dataset files:\", path)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=1121 execution_start=1769550425171 id="sC6affodYB7R" outputId="027f09f3-46ae-4c51-c923-a0936d94f6ed" source_hash="7b09edc6"
# Kaggle: сваляне на датасета чрез kagglehub
import kagglehub

# Download latest version
path = kagglehub.dataset_download("thedevastator/spotify-tracks-genre-dataset")

print("Path to dataset files:", path)


# %% cell_id="1c371fdcf3b34d8bb2defa8edf5829be" deepnote_app_block_group_id deepnote_app_block_order=6 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="029282de92cd4f2cbc248e3ad05822ce" deepnote_cell_type="code" deepnote_content_hash="632f1b13" deepnote_execution_finished_at="2026-01-27T20:25:48.242Z" deepnote_execution_started_at="2026-01-27T20:25:48.151Z" deepnote_sorting_key="9" deepnote_source="!ls /root/.cache/kagglehub/datasets/thedevastator/spotify-tracks-genre-dataset/versions/1" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=91 execution_start=1769545548151 id="dM2K7rwxYB7S" outputId="bcd205ae-3e48-483c-f8f3-8508159fdcf8" source_hash="632f1b13"
# kagglehub
# !ls /root/.cache/kagglehub/datasets/thedevastator/spotify-tracks-genre-dataset/versions/1

# %% cell_id="da89c73b27d940778c52c96f6e727cab" deepnote_app_block_group_id deepnote_app_block_order=7 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b3edfdac08594ff48d21af698feb86b7" deepnote_cell_type="code" deepnote_content_hash="1f94353e" deepnote_execution_finished_at="2026-01-27T21:47:10.899Z" deepnote_execution_started_at="2026-01-27T21:47:10.524Z" deepnote_sorting_key="10" deepnote_source="df = pd.read_csv(path + '/train.csv', index_col=0)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=375 execution_start=1769550430524 id="gXDmn4tvYB7S" source_hash="1f94353e"
# kagglehub
df = pd.read_csv(path + '/train.csv', index_col=0)

# %% cell_id="a496a2251bc44d1a8f235dbfeed294a8" deepnote_block_group="0592c33a4e3e4179be0693a6473e37d8" deepnote_cell_type="code" deepnote_content_hash="14f60b8f" deepnote_execution_finished_at="2026-01-27T20:25:48.651Z" deepnote_execution_started_at="2026-01-27T20:25:48.651Z" deepnote_sorting_key="11" deepnote_source="df.shape" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548651 id="iAmMqeasYB7S" outputId="ee3de8cb-101f-401a-ffcd-8a568733f463" source_hash="14f60b8f"
df.shape

# %% cell_id="2fcf49e86b734a51b4609dd1cbd432a3" deepnote_app_block_group_id deepnote_app_block_order=8 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="4abaa37a99e248b399fc9d6efc215898" deepnote_cell_type="code" deepnote_content_hash="f804c160" deepnote_execution_finished_at="2026-01-27T20:25:48.701Z" deepnote_execution_started_at="2026-01-27T20:25:48.701Z" deepnote_sorting_key="12" deepnote_source="df" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548701 id="MWpAFyyUYB7S" outputId="5953bd74-69af-4a4f-afe0-3076c71c849d" source_hash="f804c160"
df

# %% cell_id="65dfeb04f3b24e1cbc55b1c3be13be98" deepnote_app_block_group_id deepnote_app_block_order=9 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="ec9c7b7e4b5a4a698837d4b23d80bb74" deepnote_cell_type="code" deepnote_content_hash="f9e39fdf" deepnote_execution_finished_at="2026-01-27T20:25:48.781Z" deepnote_execution_started_at="2026-01-27T20:25:48.781Z" deepnote_sorting_key="13" deepnote_source="np.unique(df['track_genre'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548781 id="ZoVMJsMMYB7S" outputId="8e3a7a3f-5539-491c-d7e6-3e0ee752fa35" source_hash="f9e39fdf"
np.unique(df['track_genre'])

# %% cell_id="8f67056ec7a14c3080ad94b5840a7e19" deepnote_app_block_group_id deepnote_app_block_order=10 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="be1370a7815448cab2deb7669c1a5987" deepnote_cell_type="code" deepnote_content_hash="eeb3f9d8" deepnote_execution_finished_at="2026-01-27T20:25:49.704Z" deepnote_execution_started_at="2026-01-27T20:25:48.831Z" deepnote_sorting_key="14" deepnote_source="# Set a larger figure size so the list fits\nplt.figure(figsize=(12, 20)) \n\nplt.title(\"Distribution of tracks per genres\")\n# Swap x and y (put genre on Y-axis)\nsns.countplot(y='track_genre', data=df) \n# OR if using barplot: sns.barplot(x='popularity', y='track_genre', data=df)\n\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=873 execution_start=1769545548831 id="uaZoktlfYB7S" outputId="ffcd14c2-9819-4c0b-fc72-9a04bf5b3b21" source_hash="eeb3f9d8"
# Set a larger figure size so the list fits
plt.figure(figsize=(12, 20))

plt.title("Distribution of tracks per genres")
# Swap x and y (put genre on Y-axis)
sns.countplot(y='track_genre', data=df)
# OR if using barplot: sns.barplot(x='popularity', y='track_genre', data=df)

plt.show()

# %% cell_id="100e5efccba444c9857c026d2754fa15" deepnote_app_block_group_id deepnote_app_block_order=11 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="3d650264fd324687bc541b052b910e02" deepnote_cell_type="code" deepnote_content_hash="dbc998a9" deepnote_execution_finished_at="2026-01-27T20:25:49.996Z" deepnote_execution_started_at="2026-01-27T20:25:49.761Z" deepnote_sorting_key="15" deepnote_source="plt.figure(figsize=(20, 5))\nsns.boxplot(data=df, x='duration_ms')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=235 execution_start=1769545549761 id="ykKMS1g2YB7T" outputId="d56794c5-aa85-4363-9c95-a3fbb733dd8a" source_hash="dbc998a9"
plt.figure(figsize=(20, 5))
sns.boxplot(data=df, x='duration_ms')
plt.show()

# %% cell_id="0d9cd2d9adb447209bc9c4cf82f5a232" deepnote_app_block_group_id deepnote_app_block_order=12 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="64146747b61549a0a3a5e52769883a3d" deepnote_cell_type="code" deepnote_content_hash="4d04b885" deepnote_execution_finished_at="2026-01-27T20:25:50.041Z" deepnote_execution_started_at="2026-01-27T20:25:50.041Z" deepnote_sorting_key="16" deepnote_source="if df.isnull().values.any():\n    print(\"Missing values found!\")\n    print(\"-\" * 30)\n    # Show count of NaNs per column\n    print(df.isnull().sum())\nelse:\n    print(\"No missing values found in the DataFrame.\")" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545550041 id="y9J6XRQXYB7T" outputId="210f4960-f3e8-4e67-f762-6abd3c523d74" source_hash="4d04b885"
if df.isnull().values.any():
    print("Missing values found!")
    print("-" * 30)
    # Show count of NaNs per column
    print(df.isnull().sum())
else:
    print("No missing values found in the DataFrame.")

# %% cell_id="2ec38365549f4eef8a21af3fb2352848" deepnote_app_block_group_id deepnote_app_block_order=13 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="77b188c1d223447d9906ab113414ef18" deepnote_cell_type="code" deepnote_content_hash="25d43fa0" deepnote_execution_finished_at="2026-01-27T20:25:50.101Z" deepnote_execution_started_at="2026-01-27T20:25:50.101Z" deepnote_sorting_key="17" deepnote_source="df.columns" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545550101 id="Etnk4KecYB7T" outputId="48e670d5-9d84-4d05-a739-50d4cfeefd0d" source_hash="25d43fa0"
df.columns

# %% cell_id="5e3011cf86514a05a3f45ebf5c88eda7" deepnote_app_block_group_id deepnote_app_block_order=14 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="00a945ab35094ba694655233f74bd163" deepnote_cell_type="code" deepnote_content_hash="7f1878dd" deepnote_execution_finished_at="2026-01-27T20:25:50.861Z" deepnote_execution_started_at="2026-01-27T20:25:50.161Z" deepnote_sorting_key="18" deepnote_source="sns.histplot(x=df['danceability'], kde=True, bins='auto')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=700 execution_start=1769545550161 id="vq-DKXldYB7T" outputId="9a65da59-b4ac-41fd-8e94-44e9cf55e458" source_hash="7f1878dd"
sns.histplot(x=df['danceability'], kde=True, bins='auto')
plt.show()

# %% cell_id="949758369c1c4ddf89b1dcb08226f991" deepnote_app_block_group_id deepnote_app_block_order=15 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="f7a005f68b454716bdd2d8b4e2f44f39" deepnote_cell_type="code" deepnote_content_hash="15a58f46" deepnote_execution_finished_at="2026-01-27T20:25:51.491Z" deepnote_execution_started_at="2026-01-27T20:25:50.911Z" deepnote_sorting_key="19" deepnote_source="sns.histplot(x=df['energy'], kde=True, bins='auto')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=580 execution_start=1769545550911 id="EP3GGNnwYB7T" outputId="9f9eb617-397f-468e-c044-b5d20fa52d57" source_hash="15a58f46"
sns.histplot(x=df['energy'], kde=True, bins='auto')
plt.show()

# %% cell_id="5018ecddc6b143a7a97df2ed4a438196" deepnote_app_block_group_id deepnote_app_block_order=16 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="4fb74fcd6951406cb3afafac01cbd2bc" deepnote_cell_type="code" deepnote_content_hash="eb8966df" deepnote_execution_finished_at="2026-01-27T20:25:51.541Z" deepnote_execution_started_at="2026-01-27T20:25:51.541Z" deepnote_sorting_key="20" deepnote_source="df['explicit'].value_counts().plot(kind='bar', color=['red', 'green'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545551541 id="NNFcZiTMYB7U" outputId="332ea447-00fc-4f45-8142-c9d888d7e2e5" source_hash="eb8966df"
df['explicit'].value_counts().plot(kind='bar', color=['red', 'green'])

# %% cell_id="80a90f261f4441e1a9f643277b7c33ab" deepnote_app_block_group_id deepnote_app_block_order=17 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1d46b2b139b649b497527c3dfff9f02b" deepnote_cell_type="code" deepnote_content_hash="11a9c500" deepnote_execution_finished_at="2026-01-27T20:25:51.718Z" deepnote_execution_started_at="2026-01-27T20:25:51.661Z" deepnote_sorting_key="21" deepnote_source="df['mode'].value_counts().plot(kind='bar')\nplt.xticks(ticks=[0, 1], labels=['minor', 'major'])\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=57 execution_start=1769545551661 id="nUVGUMUFYB7U" outputId="3485423f-44c2-4f5b-c5cc-ee7cf5edd0dc" source_hash="11a9c500"
df['mode'].value_counts().plot(kind='bar')
plt.xticks(ticks=[0, 1], labels=['minor', 'major'])
plt.show()

# %% cell_id="21184c4631df4fc38c840e17f921c1d0" deepnote_app_block_group_id deepnote_app_block_order=18 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1413a34a3aea4904aa20b9a8466918bf" deepnote_cell_type="code" deepnote_content_hash="c33227cf" deepnote_execution_finished_at="2026-01-27T20:25:51.771Z" deepnote_execution_started_at="2026-01-27T20:25:51.771Z" deepnote_sorting_key="22" deepnote_source="np.unique(df['key'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545551771 id="ZK6Qv3CzYB7U" outputId="e79713f7-1672-4135-be48-62385becb20b" source_hash="c33227cf"
np.unique(df['key'])

# %% cell_id="60fababd386a4cfab2ec0fc6d039af74" deepnote_app_block_group_id deepnote_app_block_order=19 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="febfd683232c489b961ee9884a9e7219" deepnote_cell_type="code" deepnote_content_hash="81f6827a" deepnote_execution_finished_at="2026-01-27T20:25:51.892Z" deepnote_execution_started_at="2026-01-27T20:25:51.821Z" deepnote_sorting_key="23" deepnote_source="key_map = {\n    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', \n    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'\n}\n\ndf['key_name'] = df['key'].map(key_map)\n\ndf['key_name'].value_counts().sort_index().plot(kind='bar')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=71 execution_start=1769545551821 id="mV-cbapLYB7U" outputId="45113773-c7d6-4312-f32e-e2e6eeedd837" source_hash="81f6827a"
key_map = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F',
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

df['key_name'] = df['key'].map(key_map)

df['key_name'].value_counts().sort_index().plot(kind='bar')
plt.show()

# %% cell_id="ce698f31a3f64f20a880b9c6d34b5a93" deepnote_app_block_group_id deepnote_app_block_order=20 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="5157d4f03b5d44b9874933a6a81b319c" deepnote_cell_type="code" deepnote_content_hash="8ccda497" deepnote_execution_finished_at="2026-01-27T20:25:52.682Z" deepnote_execution_started_at="2026-01-27T20:25:52.131Z" deepnote_sorting_key="24" deepnote_source="sns.histplot(x=df['tempo'], kde=True)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=551 execution_start=1769545552131 id="tGSiF_BOYB7U" outputId="e31cc0f6-1d9f-4dd0-d344-c9e342e2b810" source_hash="8ccda497"
sns.histplot(x=df['tempo'], kde=True)

# %% cell_id="69207c260f7545398eaa727b003609a9" deepnote_app_block_group_id deepnote_app_block_order=21 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="620b1255fc5041f19d7fd52dafc2c6f1" deepnote_cell_type="code" deepnote_content_hash="48fb3ce1" deepnote_execution_finished_at="2026-01-27T20:25:52.813Z" deepnote_execution_started_at="2026-01-27T20:25:52.711Z" deepnote_sorting_key="25" deepnote_source="key_mode_pivot = pd.crosstab(df['key'], df['mode'])\n\nkey_mode_pivot.index = key_map.values()\nkey_mode_pivot.columns = ['Minor', 'Major']\n\nsns.heatmap(key_mode_pivot, annot=True, fmt='d', cmap='YlGnBu')\nplt.title('Frequency of Musical Keys by Mode')" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=102 execution_start=1769545552711 id="mdUHpqKIYB7U" outputId="b76396f1-2a37-4027-f5c5-9ade2a32adf6" source_hash="48fb3ce1"
key_mode_pivot = pd.crosstab(df['key'], df['mode'])

key_mode_pivot.index = key_map.values()
key_mode_pivot.columns = ['Minor', 'Major']

sns.heatmap(key_mode_pivot, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Frequency of Musical Keys by Mode')

# %% cell_id="2350c398aa094d8186b339b34ba18530" deepnote_app_block_group_id deepnote_app_block_order=22 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="ba12533b624c466e82febaabb84c820f" deepnote_cell_type="code" deepnote_content_hash="ff9e70a4" deepnote_execution_finished_at="2026-01-27T20:25:53.729Z" deepnote_execution_started_at="2026-01-27T20:25:53.041Z" deepnote_sorting_key="26" deepnote_source="mode_dist = pd.crosstab(df['track_genre'], df['mode'], normalize='index')\nmode_dist.columns = ['Minor', 'Major']\nmode_dist = mode_dist.sort_values('Major', ascending=False)\nmode_dist.plot(kind='barh', stacked=True, figsize=(10, 25), color=['#e74c3c', '#3498db'])\n\nplt.title('Distribution (Part) of Major vs Minor Mode per Genre')\nplt.xlabel('Proportion (0.0 to 1.0)')\nplt.ylabel('Genre')\nplt.legend(title='Musical Mode', bbox_to_anchor=(1.05, 1), loc='upper left')\nplt.axvline(x=0.5, color='white', linestyle='--', alpha=0.5) # Center line for balance\nplt.tight_layout()\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=688 execution_start=1769545553041 id="jFEDBkQTYB7U" outputId="cf94e5f2-810d-4b12-e36c-26baad53da41" source_hash="ff9e70a4"
mode_dist = pd.crosstab(df['track_genre'], df['mode'], normalize='index')
mode_dist.columns = ['Minor', 'Major']
mode_dist = mode_dist.sort_values('Major', ascending=False)
mode_dist.plot(kind='barh', stacked=True, figsize=(10, 25), color=['#e74c3c', '#3498db'])

plt.title('Distribution (Part) of Major vs Minor Mode per Genre')
plt.xlabel('Proportion (0.0 to 1.0)')
plt.ylabel('Genre')
plt.legend(title='Musical Mode', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.axvline(x=0.5, color='white', linestyle='--', alpha=0.5) # Center line for balance
plt.tight_layout()
plt.show()

# %% cell_id="501402681fc74736bc9cd5c63e6fec10" deepnote_app_block_group_id deepnote_app_block_order=23 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1e56b7cbccbb44a98dfa0740a6527bed" deepnote_cell_type="code" deepnote_content_hash="625f22c7" deepnote_execution_finished_at="2026-01-27T20:25:53.781Z" deepnote_execution_started_at="2026-01-27T20:25:53.781Z" deepnote_sorting_key="27" deepnote_source="numerical_cols = ['danceability', 'energy', 'loudness', 'speechiness', \n                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545553781 id="jpjfeIpbYB7V" source_hash="625f22c7"
numerical_cols = ['danceability', 'energy', 'loudness', 'speechiness',
                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

# %% cell_id="84e5a868e3d54777856c695d9c91ea49" deepnote_app_block_group_id deepnote_app_block_order=24 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="610f0f27d01e4e388f1fe4e7b7ac67de" deepnote_cell_type="code" deepnote_content_hash="47642bda" deepnote_execution_finished_at="2026-01-27T20:26:16.694Z" deepnote_execution_started_at="2026-01-27T20:25:53.831Z" deepnote_sorting_key="28" deepnote_source="sns.pairplot(df[numerical_cols], plot_kws={'alpha': 0.1, 's': 5}, diag_kind='kde')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=22863 execution_start=1769545553831 id="pjEtg9IWYB7V" outputId="8bbeb314-9e16-495f-f200-9a88e9bb201e" source_hash="47642bda"
sns.pairplot(df[numerical_cols], plot_kws={'alpha': 0.1, 's': 5}, diag_kind='kde')
plt.show()

# %% cell_id="9969ccca90c04e9b85507ab93805fbaf" deepnote_app_block_group_id deepnote_app_block_order=25 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="2868c2bbe7f54eb9a9a3369a19f42b6a" deepnote_cell_type="code" deepnote_content_hash="920d6848" deepnote_execution_finished_at="2026-01-27T20:26:17.760Z" deepnote_execution_started_at="2026-01-27T20:26:16.700Z" deepnote_sorting_key="29" deepnote_source="plt.figure(figsize=(40, 15))\nsns.boxplot(x='track_genre', y='energy', data=df)\nplt.title('Strong Signal: Energy Distribution by Genre')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1060 execution_start=1769545576700 id="1ihTltW1YB7V" outputId="57afa405-f8f0-46d2-f97f-ea24c81dd21c" source_hash="920d6848"
plt.figure(figsize=(40, 15))
sns.boxplot(x='track_genre', y='energy', data=df)
plt.title('Strong Signal: Energy Distribution by Genre')
plt.show()

# %% cell_id="daa3f793ae2a42c2baf102b2245a25e9" deepnote_app_block_group_id deepnote_app_block_order=26 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="671993eca58649c9810dccc9e3728eeb" deepnote_cell_type="code" deepnote_content_hash="80d00cd3" deepnote_execution_finished_at="2026-01-27T20:26:18.064Z" deepnote_execution_started_at="2026-01-27T20:26:17.821Z" deepnote_sorting_key="30" deepnote_source="plt.figure(figsize=(10, 8))\ncorr = df[numerical_cols].corr()\nsns.heatmap(corr, annot=True, fmt=\".2f\", cmap='coolwarm')\nplt.title('Feature Correlation Heatmap')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=243 execution_start=1769545577821 id="6n42yXrzYB7V" outputId="7ea5f55c-341e-40cb-ccb2-3606af149a9a" source_hash="80d00cd3"
plt.figure(figsize=(10, 8))
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# %% cell_id="58bfd240f9144ba4a02a29fd30186f2e" deepnote_app_block_group_id deepnote_app_block_order=27 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="548efb1cb7134596b067c3a4b3ded594" deepnote_cell_type="code" deepnote_content_hash="38d71b6a" deepnote_execution_finished_at="2026-01-27T20:26:18.447Z" deepnote_execution_started_at="2026-01-27T20:26:18.121Z" deepnote_sorting_key="31" deepnote_source="df_vis = df.loc[(df['track_genre'] == 'black-metal') | (df['track_genre'] == 'indian') | (df['track_genre'] == 'sleep'), numerical_cols + ['track_genre']]\n\nscaler = StandardScaler()\nscaled_features = scaler.fit_transform(df_vis[numerical_cols])\n\npca = PCA(n_components=2)\npca_result = pca.fit_transform(scaled_features)\n\nplt.figure(figsize=(10, 7))\nsns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=df_vis['track_genre'], palette='viridis')\nplt.title('PCA Projection: Do the genres separate naturally?')\nplt.xlabel('Principal Component 1')\nplt.ylabel('Principal Component 2')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=326 execution_start=1769545578121 id="JXf3IDnyYB7V" outputId="d989c7b5-9277-4c41-82c9-5fd009c6f4cc" source_hash="38d71b6a"
df_vis = df.loc[(df['track_genre'] == 'black-metal') | (df['track_genre'] == 'indian') | (df['track_genre'] == 'sleep'), numerical_cols + ['track_genre']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_vis[numerical_cols])

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_features)

plt.figure(figsize=(10, 7))
sns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=df_vis['track_genre'], palette='viridis')
plt.title('PCA Projection: Do the genres separate naturally?')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

# %% cell_id="e98810a7b7744a1d832e5fc84b25f76c" deepnote_app_block_group_id deepnote_app_block_order=28 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b0e81cbe825944b4a48e7f4721c1d7d5" deepnote_cell_type="code" deepnote_content_hash="26b75ea6" deepnote_execution_finished_at="2026-01-27T20:26:18.806Z" deepnote_execution_started_at="2026-01-27T20:26:18.501Z" deepnote_sorting_key="32" deepnote_source="target_genres = ['rock', 'classical', 'indian']\nsubset = df[df['track_genre'].isin(target_genres)].copy()\n\nscaler = MinMaxScaler()\nsubset[numerical_cols] = scaler.fit_transform(subset[numerical_cols])\n\nmeans = subset.groupby('track_genre')[numerical_cols].mean().reset_index()\n\nN = len(numerical_cols)\nangles = [n / float(N) * 2 * np.pi for n in range(N)]\nangles += angles[:1] # Close the loop\n\nfig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))\n\nfor index, row in means.iterrows():\n    values = row[numerical_cols].tolist()\n    values += values[:1]\n    ax.plot(angles, values, linewidth=1, linestyle='solid', label=row['track_genre'])\n    ax.fill(angles, values, alpha=0.1)\n\nplt.xticks(angles[:-1], numerical_cols)\nplt.title('Audio Feature Profile: Rock vs Classical vs Indian')\nplt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=305 execution_start=1769545578501 id="x-DOA0pXYB7V" outputId="7bd35ee3-3735-4264-d0cf-0399cc7ee9fd" source_hash="26b75ea6"
target_genres = ['rock', 'classical', 'indian']
subset = df[df['track_genre'].isin(target_genres)].copy()

scaler = MinMaxScaler()
subset[numerical_cols] = scaler.fit_transform(subset[numerical_cols])

means = subset.groupby('track_genre')[numerical_cols].mean().reset_index()

N = len(numerical_cols)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1] # Close the loop

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

for index, row in means.iterrows():
    values = row[numerical_cols].tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=row['track_genre'])
    ax.fill(angles, values, alpha=0.1)

plt.xticks(angles[:-1], numerical_cols)
plt.title('Audio Feature Profile: Rock vs Classical vs Indian')
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()

# %% [markdown] cell_id="dfa413c245ba453e80bebeba07bc12fa" deepnote_app_block_group_id deepnote_app_block_order=29 deepnote_app_block_visible=true deepnote_block_group="46b4f4ae204b470d946f165187116194" deepnote_cell_type="text-cell-p" deepnote_sorting_key="33" deepnote_source="Somehow indian music is close to rock xD" formattedRanges=[] id="UZHIxQmBYB7W"
# Somehow indian music is close to rock xD

# %% cell_id="c1014e9422f74f9aaa0e996f9102c997" deepnote_app_block_group_id deepnote_app_block_order=30 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="619cfc5737654e17ae282caecaf2caf4" deepnote_cell_type="code" deepnote_content_hash="63087d59" deepnote_execution_finished_at="2026-01-27T20:26:32.460Z" deepnote_execution_started_at="2026-01-27T20:26:18.871Z" deepnote_sorting_key="34" deepnote_source="results = []\n\nprint(\"--- Calculating Signal Strength (Effect Size) ---\")\n\nfor feature in numerical_cols:\n    groups = [df[df['track_genre'] == g][feature].values for g in df['track_genre'].unique()]\n    \n    # Run One-Way ANOVA\n    f_stat, p_val = stats.f_oneway(*groups)\n    \n    # Calculate Eta-Squared (Effect Size)\n    # SS_between = sum(n_i * (mean_i - grand_mean)^2)\n    # SS_total = sum((x - grand_mean)^2)\n    \n    grand_mean = df[feature].mean()\n    ss_total = np.sum((df[feature] - grand_mean)**2)\n    \n    ss_between = 0\n    for g in df['track_genre'].unique():\n        group_data = df[df['track_genre'] == g][feature]\n        n_i = len(group_data)\n        mean_i = group_data.mean()\n        ss_between += n_i * (mean_i - grand_mean)**2\n        \n    eta_squared = ss_between / ss_total\n    \n    results.append({\n        'Feature': feature,\n        'F-Statistic': f_stat,\n        'P-Value': p_val,\n        'Signal Strength (Eta^2)': eta_squared,\n        'is_significant': \"Significant Difference\" if p_val < 0.05 else \"Same Distribution\"\n    })\n\nstats_df = pd.DataFrame(results).sort_values(by='Signal Strength (Eta^2)', ascending=False)\n\nprint(stats_df[['Feature', 'Signal Strength (Eta^2)', 'P-Value', 'is_significant']].to_string(index=False))\n\nplt.figure(figsize=(10, 5))\nsns.barplot(x='Signal Strength (Eta^2)', y='Feature', data=stats_df, hue='Feature', legend=False)\nplt.title('Which Features Separate Genres Best? (Based on ANOVA Effect Size)')\nplt.xlabel('Eta-Squared (0 = No Signal, 1 = Perfect Separation)')\nplt.axvline(x=0.14, color='red', linestyle='--', label='Strong Effect Threshold (0.14)')\nplt.legend()\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=13589 execution_start=1769545578871 id="Qiv-pEj8YB7W" outputId="861d36dc-47b4-41bf-8ced-271d68b88a3c" source_hash="63087d59"
results = []

print("--- Calculating Signal Strength (Effect Size) ---")

for feature in numerical_cols:
    groups = [df[df['track_genre'] == g][feature].values for g in df['track_genre'].unique()]

    # Run One-Way ANOVA
    f_stat, p_val = stats.f_oneway(*groups)

    # Calculate Eta-Squared (Effect Size)
    # SS_between = sum(n_i * (mean_i - grand_mean)^2)
    # SS_total = sum((x - grand_mean)^2)

    grand_mean = df[feature].mean()
    ss_total = np.sum((df[feature] - grand_mean)**2)

    ss_between = 0
    for g in df['track_genre'].unique():
        group_data = df[df['track_genre'] == g][feature]
        n_i = len(group_data)
        mean_i = group_data.mean()
        ss_between += n_i * (mean_i - grand_mean)**2

    eta_squared = ss_between / ss_total

    results.append({
        'Feature': feature,
        'F-Statistic': f_stat,
        'P-Value': p_val,
        'Signal Strength (Eta^2)': eta_squared,
        'is_significant': "Significant Difference" if p_val < 0.05 else "Same Distribution"
    })

stats_df = pd.DataFrame(results).sort_values(by='Signal Strength (Eta^2)', ascending=False)

print(stats_df[['Feature', 'Signal Strength (Eta^2)', 'P-Value', 'is_significant']].to_string(index=False))

plt.figure(figsize=(10, 5))
sns.barplot(x='Signal Strength (Eta^2)', y='Feature', data=stats_df, hue='Feature', legend=False)
plt.title('Which Features Separate Genres Best? (Based on ANOVA Effect Size)')
plt.xlabel('Eta-Squared (0 = No Signal, 1 = Perfect Separation)')
plt.axvline(x=0.14, color='red', linestyle='--', label='Strong Effect Threshold (0.14)')
plt.legend()
plt.show()

# %% cell_id="10ac9e61eb1e47a8ac054ce70ae8e6a6" deepnote_app_block_group_id deepnote_app_block_order=31 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b919ef63cfbb455c91c77f4020f71320" deepnote_cell_type="code" deepnote_content_hash="8ea4c955" deepnote_execution_finished_at="2026-01-27T20:26:32.997Z" deepnote_execution_started_at="2026-01-27T20:26:32.531Z" deepnote_sorting_key="35" deepnote_source="top_feature = stats_df.iloc[0]['Feature']\n\nprint(f\"\\n--- Running Tukey's HSD for the Top Signal: {top_feature} ---\")\n\ngenres_for_test = ['classical', 'rock', 'black-metal', 'indian', 'sleep']\ndf_test = df[df['track_genre'].isin(genres_for_test)]\n\ntukey = pairwise_tukeyhsd(endog=df_test[top_feature],\n                          groups=df_test['track_genre'],\n                          alpha=0.05)\n\nprint(tukey.summary())\n\nfig = tukey.plot_simultaneous(figsize=(12, 6))\nplt.title(f'Tukey HSD: Comparing Mean {top_feature.capitalize()}')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=466 execution_start=1769545592531 id="JMT9TmqKYB7W" outputId="ef6e6f29-a1a0-4a26-a55b-d21c6958fb18" source_hash="8ea4c955"
top_feature = stats_df.iloc[0]['Feature']

print(f"\n--- Running Tukey's HSD for the Top Signal: {top_feature} ---")

genres_for_test = ['classical', 'rock', 'black-metal', 'indian', 'sleep']
df_test = df[df['track_genre'].isin(genres_for_test)]

tukey = pairwise_tukeyhsd(endog=df_test[top_feature],
                          groups=df_test['track_genre'],
                          alpha=0.05)

print(tukey.summary())

fig = tukey.plot_simultaneous(figsize=(12, 6))
plt.title(f'Tukey HSD: Comparing Mean {top_feature.capitalize()}')
plt.show()

# %% cell_id="00459cadaa0f4dbb94bf6bf1ae3e211d" deepnote_app_block_group_id deepnote_app_block_order=32 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="a8cbeb987f9c446da87bf50229760514" deepnote_cell_type="code" deepnote_content_hash="886180a2" deepnote_execution_finished_at="2026-01-27T20:26:33.408Z" deepnote_execution_started_at="2026-01-27T20:26:33.051Z" deepnote_sorting_key="36" deepnote_source="top_feature2 = stats_df.iloc[1]['Feature']\nprint(f\"\\n--- Running Tukey's HSD for the Top Signal: {top_feature2} ---\")\ntukey2 = pairwise_tukeyhsd(endog=df_test[top_feature2],      \n                          groups=df_test['track_genre'],   \n                          alpha=0.05)                 \n\nprint(tukey2.summary())\n\nfig = tukey2.plot_simultaneous(figsize=(12, 6))\nplt.title(f'Tukey HSD: Comparing Mean {top_feature2.capitalize()}')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=357 execution_start=1769545593051 id="AuiTOTIKYB7W" outputId="dba5b942-873c-46d0-deae-fd1e537a51e9" source_hash="886180a2"
top_feature2 = stats_df.iloc[1]['Feature']
print(f"\n--- Running Tukey's HSD for the Top Signal: {top_feature2} ---")
tukey2 = pairwise_tukeyhsd(endog=df_test[top_feature2],
                          groups=df_test['track_genre'],
                          alpha=0.05)

print(tukey2.summary())

fig = tukey2.plot_simultaneous(figsize=(12, 6))
plt.title(f'Tukey HSD: Comparing Mean {top_feature2.capitalize()}')
plt.show()

# %% cell_id="6517d383bd034961b8f40ca61d0203b3" deepnote_app_is_output_hidden=true deepnote_block_group="3df79550cb594508bcca1cabee30fe3b" deepnote_cell_type="code" deepnote_content_hash="5bab03ff" deepnote_execution_finished_at="2026-01-27T20:26:35.360Z" deepnote_execution_started_at="2026-01-27T20:26:33.481Z" deepnote_sorting_key="37" deepnote_source="tukey = pairwise_tukeyhsd(endog=df[top_feature],\n                          groups=df['track_genre'],\n                          alpha=0.05)\nprint(tukey.summary())" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1879 execution_start=1769545593481 id="f49VC6SpYB7W" is_output_hidden=true outputId="cc372770-2f1b-455f-fe84-fce87c3ac049" source_hash="5bab03ff"
tukey = pairwise_tukeyhsd(endog=df[top_feature],
                          groups=df['track_genre'],
                          alpha=0.05)
print(tukey.summary())

# %% cell_id="1ee43146192c4c428a4647819cf04caf" deepnote_app_is_output_hidden=true deepnote_block_group="2d339402389341399799420c21d6214e" deepnote_cell_type="code" deepnote_content_hash="67a0b53d" deepnote_execution_finished_at="2026-01-27T20:26:37.081Z" deepnote_execution_started_at="2026-01-27T20:26:35.451Z" deepnote_sorting_key="38" deepnote_source="tukey2 = pairwise_tukeyhsd(endog=df[top_feature2],      \n                          groups=df['track_genre'],   \n                          alpha=0.05)                 \n\nprint(tukey2.summary())" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1630 execution_start=1769545595451 id="N3IccNZCYB7W" is_output_hidden=true outputId="36ae05bb-29c0-4c0a-a4e3-2861532c0117" source_hash="67a0b53d"
tukey2 = pairwise_tukeyhsd(endog=df[top_feature2],
                          groups=df['track_genre'],
                          alpha=0.05)

print(tukey2.summary())

# %% [markdown] cell_id="dd6cb2d040f04211960c0bc802b6fa30" deepnote_block_group="333a908a48ac44daa8669455b398a2f7" deepnote_cell_type="markdown" deepnote_sorting_key="39" deepnote_source="## \u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438\u0442\u0435 \u0438 \u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u043d\u0438\u044f EDA\n\n- **\u0420\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435 (\u0436\u0430\u043d\u0440\u043e\u0432\u0435):** \u0413\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 \u043d\u0430 \u0431\u0440\u043e\u044f \u043f\u0435\u0441\u043d\u0438 \u043f\u043e track_genre \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0432 \u043d\u0430\u0431\u043e\u0440\u0430 \u0441\u0430 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u043e (\u0432\u0441\u0438\u0447\u043a\u0438 \u0438\u043c\u0430\u0442 \u0440\u0430\u0432\u0435\u043d \u0431\u0440\u043e\u0439 \u0442\u0440\u0430\u043a\u043e\u0432\u0435). \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f, \u0437\u0430\u0449\u043e\u0442\u043e \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0440\u0438\u0441\u043a\u0430 \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0434\u0430 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0432\u0438\u0441\u043e\u043a\u0430 \u0442\u043e\u0447\u043d\u043e\u0441\u0442 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043e \u0447\u0440\u0435\u0437 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043d\u0430\u0439-\u0447\u0435\u0441\u0442\u043e \u0441\u0440\u0435\u0449\u0430\u043d\u0438\u044f \u043a\u043b\u0430\u0441.\n\n- **\u041b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438:** \u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0437\u0430 NaN \u043f\u043e\u043a\u0430\u0437\u0432\u0430 **\u043c\u0438\u043d\u0438\u043c\u0430\u043b\u043d\u0438 \u043b\u0438\u043f\u0441\u0438** \u2013 \u043f\u043e 1 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0430 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442 \u0432 `artists`, `album_name` \u0438 `track_name`, \u0430 \u0432\u0441\u0438\u0447\u043a\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u0430 \u043f\u043e\u043f\u044a\u043b\u043d\u0435\u043d\u0438. \u0422\u043e\u0432\u0430 \u043e\u0437\u043d\u0430\u0447\u0430\u0432\u0430, \u0447\u0435 \u043f\u043e\u0447\u0438\u0441\u0442\u0432\u0430\u043d\u0435\u0442\u043e \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0449\u0435 \u0431\u044a\u0434\u0435 \u043b\u0435\u0441\u043d\u043e \u0438 \u043d\u044f\u043c\u0430 \u0434\u0430 \u0438\u0437\u0438\u0441\u043a\u0432\u0430 \u0441\u043b\u043e\u0436\u043d\u0438 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0437\u0430 \u043f\u043e\u043f\u044a\u043b\u0432\u0430\u043d\u0435 \u043d\u0430 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438.\n\n- **\u0420\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438:** \u0425\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u0438\u0442\u0435 \u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438\u043c\u0430\u0442 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f:\n  - \u043d\u044f\u043a\u043e\u0438 \u0441\u0430 \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d **0\u20131** (`danceability`, `energy`, `acousticness`, `valence` \u0438 \u0434\u0440.), \u043d\u043e \u043d\u0435 \u0441\u0430 \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u0438 (\u0438\u043c\u0430 \u0441\u0442\u0440\u0443\u043f\u0432\u0430\u043d\u0435 \u0432 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u043e\u0431\u043b\u0430\u0441\u0442\u0438);\n  - tempo \u043e\u0431\u0445\u0432\u0430\u0449\u0430 \u0448\u0438\u0440\u043e\u043a \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043e\u0442 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438, \u043a\u0430\u0442\u043e \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430 \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f \u043e\u043a\u043e\u043b\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u0438 \u0442\u0435\u043c\u043f\u0430;\n  - \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 \u043d\u0430 `duration_ms` \u043f\u043e\u043a\u0430\u0437\u0432\u0430 \u0430\u0441\u0438\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0441 \u043a\u0440\u0430\u0439\u043d\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438, \u0442.\u0435. \u0438\u043c\u0430 \u0438 \u043d\u0435\u043e\u0431\u0438\u0447\u0430\u0439\u043d\u043e \u0434\u044a\u043b\u0433\u0438 \u0437\u0430\u043f\u0438\u0441\u0438, \u043a\u043e\u0435\u0442\u043e \u0435 \u043d\u043e\u0440\u043c\u0430\u043b\u043d\u043e \u0437\u0430 \u0440\u0435\u0430\u043b\u043d\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0434\u0430\u043d\u043d\u0438.\n\n- **\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0438:** `explicit` \u0435 \u0434\u0438\u0441\u0431\u0430\u043b\u0430\u043d\u0441\u0438\u0440\u0430\u043d\u0430 (\u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u043f\u0435\u0441\u043d\u0438 \u0441\u0430 False), \u0434\u043e\u043a\u0430\u0442\u043e `mode` (major/minor) \u043f\u043e\u043a\u0430\u0437\u0432\u0430 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043f\u0440\u0438 \u0440\u0430\u0437\u0431\u0438\u0432\u043a\u0430 \u043f\u043e \u0436\u0430\u043d\u0440.\n\n- **\u201eKey\u201c \u0438 \u201eMode\u201c \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:** \u0421\u043b\u0435\u0434 \u043c\u0430\u043f\u0432\u0430\u043d\u0435\u0442\u043e \u043d\u0430 `key` \u043a\u044a\u043c \u0438\u043c\u0435\u043d\u0430 (C, C#, D, \u2026) \u0438 crosstab/heatmap \u0441\u0435 \u0432\u0438\u0436\u0434\u0430, \u0447\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u0442\u043e\u043d\u0430\u043b\u043d\u043e\u0441\u0442\u0438 \u0441\u0435 \u0441\u0440\u0435\u0449\u0430\u0442 \u043f\u043e-\u0447\u0435\u0441\u0442\u043e, \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u043d\u0435\u0442\u043e \u043d\u0430 `key` \u0437\u0430\u0435\u0434\u043d\u043e \u0441 `mode` \u0434\u0430\u0432\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442. \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u043a\u0430\u0442\u043e \u043e\u0441\u043e\u0431\u0435\u043d\u043e\u0441\u0442, \u043d\u043e \u043d\u044f\u043c\u0430 \u0434\u0430 \u0435 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u0438\u044f\u0442 \u0441\u0438\u043b\u0435\u043d \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435.\n\n- **\u0412\u0440\u044a\u0437\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 (\u043a\u043e\u0440\u0435\u043b\u0430\u0446\u0438\u0438):** Correlation heatmap-\u044a\u0442 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438:\n  - `energy` \u0438 `loudness` \u0441\u0430 \u0441\u0438\u043b\u043d\u043e \u0441\u0432\u044a\u0440\u0437\u0430\u043d\u0438 (\u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u0441 \u043f\u043e-\u0432\u0438\u0441\u043e\u043a\u0430 \u0435\u043d\u0435\u0440\u0433\u0438\u044f \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0438\u043c\u0430\u0442 \u0438 \u043f\u043e-\u0432\u0438\u0441\u043e\u043a\u0430 \u0441\u0438\u043b\u0430 \u043d\u0430 \u0437\u0432\u0443\u043a\u0430);\n  - `acousticness` \u0435 \u0432 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043f\u043e\u043b\u043e\u0436\u043d\u0430 \u043f\u043e\u0441\u043e\u043a\u0430 \u0441\u043f\u0440\u044f\u043c\u043e `energy`/`loudness` (\u043f\u043e-\u0430\u043a\u0443\u0441\u0442\u0438\u0447\u043d\u0438\u0442\u0435 \u043f\u0435\u0441\u043d\u0438 \u0441\u0430 \u043f\u043e-\u0442\u0438\u0445\u0438 \u0438 \u043f\u043e-\u043c\u0430\u043b\u043a\u043e \u201e\u0438\u043d\u0442\u0435\u043d\u0437\u0438\u0432\u043d\u0438\u201c);\n  - \u0438\u043c\u0430 \u0438 \u043f\u043e-\u0441\u043b\u0430\u0431\u0438/\u0443\u043c\u0435\u0440\u0435\u043d\u0438 \u0432\u0440\u044a\u0437\u043a\u0438, (\u043d\u0430\u043f\u0440. \u043c\u0435\u0436\u0434\u0443 `danceability` \u0438 `valence`) \u043a\u043e\u0438\u0442\u043e \u0441\u0430 \u0438\u043d\u0442\u0443\u0438\u0442\u0438\u0432\u043d\u043e \u043e\u0431\u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438, \u043d\u043e \u043d\u0435 \u0441\u0438\u043b\u043d\u043e \u0438\u0437\u0440\u0430\u0437\u0435\u043d\u0438.\n\n- **\u0420\u0430\u0437\u043b\u0438\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435:** Boxplot-\u0438\u0442\u0435 \u043f\u043e \u0436\u0430\u043d\u0440 (\u043d\u0430\u043f\u0440. \u0437\u0430 `energy`) \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0438\u043c\u0430\u0442 **\u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0438**, \u043d\u043e \u0441\u044a\u0449\u043e \u0438 **\u0441\u0435\u0440\u0438\u043e\u0437\u043d\u043e \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0435**. \u0422\u043e\u0432\u0430 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u044a\u0442 \u0442\u0440\u0443\u0434\u043d\u043e \u0449\u0435 \u0441\u0435 \u043e\u0442\u0434\u0435\u043b\u0438 \u0441 \u0435\u0434\u0438\u043d \u043f\u0440\u0438\u0437\u043d\u0430\u043a, \u0430 \u0449\u0435 \u0435 \u043d\u0443\u0436\u043d\u0430 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f \u043e\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449 \u043c\u043e\u0434\u0435\u043b.\n\n- **PCA \u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u0430 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u043e\u0441\u0442:** PCA \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f\u0442\u0430 (\u0441\u043b\u0435\u0434 `StandardScaler`) \u0437\u0430 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0438\u043c\u0430 **\u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435**, \u043d\u043e \u043d\u0435 \u0438 \u0438\u0434\u0435\u0430\u043b\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u2014 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e \u043f\u0440\u0438 \u0431\u043b\u0438\u0437\u043a\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0441\u0442\u0438\u043b\u043e\u0432\u0435. \u0422\u043e\u0432\u0430 \u0435 \u0434\u043e\u0431\u044a\u0440 \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440, \u0447\u0435 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0438\u043c\u0430\u0442 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430, \u043d\u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043d\u0435 \u0435 \u0442\u0440\u0438\u0432\u0438\u0430\u043b\u043d\u0430.\n\n- **\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0438 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f:** Radar \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 (\u0441\u043b\u0435\u0434 `MinMaxScaler`) \u0437\u0430 \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0438\u0440\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u0447\u0440\u0435\u0437 \u0441\u044a\u0432\u043a\u0443\u043f\u043d\u043e\u0441\u0442 \u043e\u0442 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438, \u0430 \u043d\u0435 \u0447\u0440\u0435\u0437 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u0430 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430. \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u043a\u0430\u0442\u043e \u043e\u0441\u043d\u043e\u0432\u0430 \u0438 \u0437\u0430 \u0431\u044a\u0434\u0435\u0449\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435.\n\n- **\u041a\u043e\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043d\u043e\u0441\u044f\u0442 \u043d\u0430\u0439-\u0441\u0438\u043b\u0435\u043d \u0441\u0438\u0433\u043d\u0430\u043b:** \u0415\u0444\u0435\u043a\u0442\u043d\u0438\u044f\u0442 \u0440\u0430\u0437\u043c\u0435\u0440 (eta-squared) \u0434\u0430\u0432\u0430 \u043f\u043e\u0434\u0440\u0435\u0434\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0441\u043f\u043e\u0440\u0435\u0434 \u0442\u043e\u0432\u0430 \u043a\u043e\u043b\u043a\u043e \u0441\u0438\u043b\u043d\u043e \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435. \u0422\u043e\u0432\u0430 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0434\u0430 \u0441\u0435 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u0446\u0438\u0440\u0430\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u043a\u043e\u0438\u0442\u043e \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u043f\u043e-\u0432\u0430\u0436\u043d\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u043e \u0437\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f.\n\n- **\u0414\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u043e\u043d\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437:** \u041f\u0440\u043e\u0432\u0435\u0434\u0435\u043d \u0435 ANOVA \u0442\u0435\u0441\u0442, \u0437\u0430 \u0434\u0430 \u0441\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u0438 \u0434\u0430\u043b\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\u0442\u0435 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043c\u0435\u0436\u0434\u0443 \u0433\u0440\u0443\u043f\u0438\u0442\u0435 (\u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435). \u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0440\u0430\u0437\u043b\u0438\u043a\u0438\u0442\u0435 \u043c\u0435\u0436\u0434\u0443 \u0433\u0440\u0443\u043f\u0438\u0442\u0435 \u0441\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u043d\u0430\u0447\u0438\u043c\u0438. \u0421\u043b\u0435\u0434 \u0442\u043e\u0432\u0430 \u0447\u0440\u0435\u0437 Tukey HSD \u0435 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430\u043d\u043e \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u0438 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u0438 \u0433\u0440\u0443\u043f\u0438 \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430\u0442 \u0442\u0435\u0437\u0438 \u0440\u0430\u0437\u043b\u0438\u043a\u0438. \u0410\u043d\u0430\u043b\u0438\u0437\u044a\u0442, \u0438\u0437\u0432\u044a\u0440\u0448\u0435\u043d \u0432\u044a\u0440\u0445\u0443 \u0434\u0432\u0430\u0442\u0430 \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u0430 \u0441\u043f\u043e\u0440\u0435\u0434 eta-squared, \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0432 \u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u0441\u043b\u0443\u0447\u0430\u0438 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0438\u043c\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u043d\u0430\u0447\u0438\u043c\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f.\n\n**\u0418\u0437\u0432\u043e\u0434 \u043d\u0430 \u043d\u0438\u0432\u043e EDA:** \u0414\u0430\u043d\u043d\u0438\u0442\u0435 \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u0442 \u0447\u0438\u0441\u0442\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438 \u0437\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430; \u0438\u043c\u0430 \u044f\u0441\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f. \u0422\u0435\u0437\u0438 \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f \u0434\u0430\u0432\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430 \u043f\u0440\u0438\u043b\u0430\u0433\u0430\u043d\u0435 \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435." id="gdNVJE9YYB7X"
# ## Анализ на визуализациите и първоначалния EDA
#
# - **Разпределение на класовете (жанрове):** Графиката на броя песни по track_genre показва, че жанровете в набора са представени равномерно (всички имат равен брой тракове). Това е полезно за класификация, защото намалява риска моделът да постига висока точност единствено чрез избор на най-често срещания клас.
#
# - **Липсващи стойности:** Проверка за NaN показва **минимални липси** – по 1 липсваща стойност в `artists`, `album_name` и `track_name`, а всички числови аудио характеристики са попълнени. Това означава, че почистването на данните ще бъде лесно и няма да изисква сложни техники за попълване на липсващи стойности.
#
# - **Разпределения на числовите характеристики:** Хистограмите и графиките показват, че признаците имат различни разпределения:
#   - някои са в диапазон **0–1** (`danceability`, `energy`, `acousticness`, `valence` и др.), но не са равномерни (има струпване в определени области);
#   - tempo обхваща широк диапазон от стойности, като се наблюдава концентрация около определени характерни темпа;
#   - графиката на `duration_ms` показва асиметрично разпределение с крайни стойности, т.е. има и необичайно дълги записи, което е нормално за реални музикални данни.
#
# - **Категориални променливи:** `explicit` е дисбалансирана (повечето песни са False), докато `mode` (major/minor) показва различия между жанровете при разбивка по жанр.
#
# - **„Key“ и „Mode“ контекст:** След мапването на `key` към имена (C, C#, D, …) и crosstab/heatmap се вижда, че определени тоналности се срещат по-често, разглеждането на `key` заедно с `mode` дава допълнителен музикален контекст. Това е полезно като особеност, но няма да е единственият силен разделител на жанрове.
#
# - **Връзки между признаците (корелации):** Correlation heatmap-ът подсказва очаквани зависимости:
#   - `energy` и `loudness` са силно свързани (песните с по-висока енергия обикновено имат и по-висока сила на звука);
#   - `acousticness` е в противоположна посока спрямо `energy`/`loudness` (по-акустичните песни са по-тихи и по-малко „интензивни“);
#   - има и по-слаби/умерени връзки, (напр. между `danceability` и `valence`) които са интуитивно обосновани, но не силно изразени.
#
# - **Разлики между жанровете:** Boxplot-ите по жанр (напр. за `energy`) показват, че жанровете имат **различни типични диапазони**, но също и **сериозно припокриване**. Това подсказва, че жанрът трудно ще се отдели с един признак, а ще е нужна комбинация от характеристики и подходящ модел.
#
# - **PCA и визуална разделимост:** PCA проекцията (след `StandardScaler`) за избрани жанрове показва, че има **частично групиране**, но не и идеално разделяне — очаквано при близки музикални стилове. Това е добър индикатор, че данните имат структура, но задачата не е тривиална.
#
# - **Профили по признаци и интерпретация:** Radar графиката (след `MinMaxScaler`) за няколко избрани жанра демонстрира, че жанровете могат да се различават чрез съвкупност от признаци, а не чрез единична характеристика. Това е полезно като основа и за бъдеща интерпретация на клъстери по настроение.
#
# - **Кои признаци носят най-силен сигнал:** Ефектният размер (eta-squared) дава подредба на признаците според това колко силно се различават между жанровете. Това позволява да се идентифицират характеристики, които вероятно ще бъдат по-важни за класификация и потенциално за клъстеризация.
#
# - **Дисперсионен анализ:** Проведен е ANOVA тест, за да се провери дали стойностите на параметрите се различават между групите (жанровете). Резултатите показват, че разликите между групите са статистически значими. След това чрез Tukey HSD е изследвано между кои конкретни групи се наблюдават тези разлики. Анализът, извършен върху двата най-силни признака според eta-squared, показва, че в повечето случаи между жанровете има статистически значими различия.
#
# **Извод на ниво EDA:** Данните изглеждат чисти и подходящи за проекта; има ясни зависимости между признаците и жанрови различия. Тези наблюдения дават основание за прилагане на модели за класификация на жанрове и групиране по настроение.

# %% [markdown] cell_id="da51c40b29034890a194fef1f1a2965c" deepnote_block_group="735b51333cc849ffa05cde6fa3ebbd9c" deepnote_cell_type="markdown" deepnote_sorting_key="40" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435, \u043a\u043e\u0438\u0442\u043e \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435\n\n\u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u0449\u0435 \u0432\u043a\u043b\u044e\u0447\u0432\u0430 \u0434\u0432\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 ML \u0437\u0430\u0434\u0430\u0447\u0438 \u0432\u044a\u0440\u0445\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 \u0441 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438: **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440** \u0438 **\u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435/\u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u0435\u043d \u043f\u0440\u043e\u0444\u0438\u043b**. \u0412\u0441\u0438\u0447\u043a\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u0438 \u0441\u0442\u044a\u043f\u043a\u0438 \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d\u0438 \u0441\u044a\u0441 `scikit-learn` \u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u043e\u0442 \u043a\u0443\u0440\u0441\u0430.\n\n### \u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u0436\u0430\u043d\u0440 (supervised learning)\n\u0429\u0435 \u0442\u0440\u0435\u0442\u0438\u0440\u0430\u043c\u0435 \u043a\u043e\u043b\u043e\u043d\u0430\u0442\u0430 **`track_genre`** \u043a\u0430\u0442\u043e \u0446\u0435\u043b\u0435\u0432\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0438 \u0449\u0435 \u043e\u0431\u0443\u0447\u0438\u043c \u043c\u043e\u0434\u0435\u043b\u0438, \u043a\u043e\u0438\u0442\u043e \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u0442 \u0436\u0430\u043d\u0440\u0430 \u043d\u0430 \u043f\u0435\u0441\u0435\u043d\u0442\u0430 \u043f\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043d\u0430\u043f\u0440. `danceability`, `energy`, `acousticness`, `valence`, `tempo` \u0438 \u0434\u0440.).\n\n\u041f\u043b\u0430\u043d\u0438\u0440\u0430\u043c\u0435 \u0434\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u043c \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u044a\u043c\u0430:\n- **Logistic Regression** (\u0431\u0430\u0437\u043e\u0432 \u043c\u043e\u0434\u0435\u043b);\n- **k-Nearest Neighbors (kNN)**;\n- **Support Vector Machines (SVM)**;\n- **Decision Tree / Random Forest** (\u0437\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0438 \u043f\u043e-\u043b\u0435\u0441\u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f);\n- **MLPClassifier** \u043a\u0430\u0442\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u043e\u0442 \u0443\u0447\u0435\u0431\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b.\n\n\u0429\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0438\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0438 \u0437\u0430 \u043d\u0430\u0434\u0435\u0436\u0434\u043d\u0430 \u043e\u0446\u0435\u043d\u043a\u0430:\n- \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u043d\u0430 train/test \u0438/\u0438\u043b\u0438 **cross-validation**;\n- \u043f\u043e\u0434\u0431\u043e\u0440 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0447\u0440\u0435\u0437 **GridSearchCV** \u0438\u043b\u0438 **RandomizedSearchCV**;\n- \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043a\u0430\u0442\u043e **accuracy**, **macro F1**, **Precision**, **Recall** \u0438 **confusion matrix** (\u043e\u0441\u043e\u0431\u0435\u043d\u043e \u0432\u0430\u0436\u043d\u0438 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u043a\u043b\u0430\u0441\u043e\u0432\u0435).\n\n### \u041a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 (unsupervised learning)\n\u0417\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u0442\u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u0438), \u0437\u0430 \u0434\u0430 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043c\u0435 \u043f\u0435\u0441\u043d\u0438 \u0441\u044a\u0441 \u0441\u0445\u043e\u0434\u0435\u043d \u043f\u0440\u043e\u0444\u0438\u043b.\n\n\u041f\u043b\u0430\u043d\u0438\u0440\u0430\u043c\u0435 \u0434\u0430 \u0438\u0437\u043f\u0440\u043e\u0431\u0432\u0430\u043c\u0435:\n- **KMeans** (\u043e\u0441\u043d\u043e\u0432\u0435\u043d \u043c\u0435\u0442\u043e\u0434);\n- **DBSCAN** (\u0437\u0430 \u043e\u0442\u043a\u0440\u0438\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u043e-\u0441\u043b\u043e\u0436\u043d\u0438 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438 \u0438 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u0438 \u0430\u0443\u0442\u043b\u0430\u0439\u0435\u0440\u0438);\n- *(\u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0448\u0438\u0440\u0435\u043d\u0438\u0435)* **Agglomerative Clustering** \u043a\u0430\u0442\u043e \u0430\u043b\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u0430 \u043d\u0430 KMeans/DBSCAN.\n\n\u0417\u0430 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0438 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0442\u0435 \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u0438 \u043e\u0442 `scikit-learn`, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:\n- **silhouette score**, **Davies\u2013Bouldin index** \u0438/\u0438\u043b\u0438 **Calinski\u2013Harabasz score** (\u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043d\u0430 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u044f);\n- \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0442\u0435 \u0447\u0440\u0435\u0437 **\u0441\u0440\u0435\u0434\u043d\u0438/\u043c\u0435\u0434\u0438\u0430\u043d\u0438 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435** \u043f\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440 \u0438 \u043e\u043f\u0438\u0441\u0432\u0430\u043d\u0435 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u201e\u043f\u0440\u043e\u0444\u0438\u043b\u0438\u201c (\u043d\u0430\u043f\u0440. \u043f\u043e `energy` \u0438 `valence`).\n\n\u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e, \u0437\u0430 \u043f\u043e-\u044f\u0441\u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043c\u0435\u0442\u043e\u0434\u0438 \u0437\u0430 \u043f\u043e\u043d\u0438\u0436\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u0442\u0430:\n- **PCA** (2D/3D \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f \u0437\u0430 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430\u0442\u0430),\n- *(\u043f\u043e \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442)* **t-SNE** \u043a\u0430\u0442\u043e \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u0430 \u0442\u0435\u0445\u043d\u0438\u043a\u0430 (\u0441\u0430\u043c\u043e \u0437\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f, \u043d\u0435 \u043a\u0430\u0442\u043e \u043c\u043e\u0434\u0435\u043b).\n" id="Ry0L-U6hYB7X"
# ## Кратко описание на алгоритмите, които ще използваме
#
# Проектът ще включва две основни ML задачи върху таблични данни с аудио характеристики на песни: **класификация на жанр** и **клъстеризация по настроение/емоционален профил**. Всички модели и стъпки ще бъдат реализирани със `scikit-learn` и стандартни техники от курса.
#
# ### Класификация на музикален жанр (supervised learning)
# Ще третираме колоната **`track_genre`** като целева променлива и ще обучим модели, които предсказват жанра на песента по числови аудио характеристики (напр. `danceability`, `energy`, `acousticness`, `valence`, `tempo` и др.).
#
# Планираме да сравним няколко класически алгоритъма:
# - **Logistic Regression** (базов модел);
# - **k-Nearest Neighbors (kNN)**;
# - **Support Vector Machines (SVM)**;
# - **Decision Tree / Random Forest** (за нелинейни зависимости и по-лесна интерпретация);
# - **MLPClassifier** като допълнителен сравнителен модел от учебния материал.
#
# Ще приложим стандартни практики за надеждна оценка:
# - разделяне на данните на train/test и/или **cross-validation**;
# - подбор на хиперпараметри чрез **GridSearchCV** или **RandomizedSearchCV**;
# - метрики за оценка като **accuracy**, **macro F1**, **Precision**, **Recall** и **confusion matrix** (особено важни при много класове).
#
# ### Клъстеризация на песни по настроение (unsupervised learning)
# За клъстеризацията по настроение ще използваме само числовите аудио характеристики (без жанровите етикети), за да групираме песни със сходен профил.
#
# Планираме да изпробваме:
# - **KMeans** (основен метод);
# - **DBSCAN** (за откриване на по-сложни структури и потенциални аутлайери);
# - *(възможно разширение)* **Agglomerative Clustering** като алтернатива на KMeans/DBSCAN.
#
# За избор на параметри и оценка на клъстерите ще използваме подходи от `scikit-learn`, например:
# - **silhouette score**, **Davies–Bouldin index** и/или **Calinski–Harabasz score** (сравнение на различни решения);
# - анализ на клъстерите чрез **средни/медиани на признаците** по клъстер и описване на типични „профили“ (напр. по `energy` и `valence`).
#
# Допълнително, за по-ясна интерпретация ще използваме методи за понижаване на размерността:
# - **PCA** (2D/3D проекция за визуализация и проверка на структурата),
# - *(по възможност)* **t-SNE** като визуална техника (само за интерпретация, не като модел).
#

# %% [markdown] cell_id="473f3aba4bba4273aabab54cfc8c97c3" deepnote_block_group="247ae8135cfb41ee90716f6e303db8d1" deepnote_cell_type="markdown" deepnote_sorting_key="41" deepnote_source="## \u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438, \u043a\u043e\u0438\u0442\u043e \u0441\u043c\u044f\u0442\u0430\u043c\u0435 \u0434\u0430 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435\n\n\u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u0449\u0435 \u0431\u044a\u0434\u0435 \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d \u043d\u0430 **Python** \u0441 **Jupyter Notebook**, \u043a\u0430\u0442\u043e \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 \u043e\u0442 \u0435\u043a\u043e\u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0442\u0430 \u0437\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 \u0438 `scikit-learn`:\n\n- **NumPy** \u2013 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0438 \u043c\u0430\u0441\u0438\u0432\u0438;\n- **Pandas** \u2013 \u0437\u0430\u0440\u0435\u0436\u0434\u0430\u043d\u0435 \u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (`CSV`), \u0444\u0438\u043b\u0442\u0440\u0438\u0440\u0430\u043d\u0435, \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438;\n- **Matplotlib** \u0438 **Seaborn** \u2013 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0437\u0430 EDA \u0438 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435;\n- **Scikit-learn** \u2013 \u043e\u0441\u043d\u043e\u0432\u043d\u0430\u0442\u0430 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430 \u0437\u0430 \u0446\u0435\u043b\u0438\u044f ML pipeline:\n  - \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430: `StandardScaler` / `MinMaxScaler`, `LabelEncoder` / `OneHotEncoder` (\u0430\u043a\u043e \u0435 \u043d\u0443\u0436\u043d\u043e),\n  - \u043c\u043e\u0434\u0435\u043b\u0438: Logistic Regression, kNN, SVM, Decision Tree / Random Forest, KMeans, DBSCAN (\u0438 \u0435\u0432\u0435\u043d\u0442\u0443\u0430\u043b\u043d\u043e Agglomerative),\n  - \u043e\u0446\u0435\u043d\u043a\u0430: \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f,\n  - \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u044f \u0438 tuning: `train_test_split`, `cross_val_score`, `GridSearchCV` / `RandomizedSearchCV`,\n  - **Pipeline** \u0438 **ColumnTransformer** (\u0437\u0430 \u043f\u043e-\u0447\u0438\u0441\u0442 \u0438 \u0432\u044a\u0437\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u043c \u043a\u043e\u0434);\n- *(\u0430\u043a\u043e \u0435 \u043d\u0443\u0436\u043d\u043e \u0437\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430 \u0447\u0430\u0441\u0442 \u043a\u0430\u0442\u043e \u043f\u0440\u0438 preliminary analysis)* **Statsmodels** \u2013 \u0437\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0442\u0435\u0441\u0442\u043e\u0432\u0435 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438;\n- **kagglehub** \u2013 \u0437\u0430 \u0438\u0437\u0442\u0435\u0433\u043b\u044f\u043d\u0435 \u043d\u0430 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u043e\u0442 Kaggle \u0432 \u0440\u0430\u0431\u043e\u0442\u043d\u0430\u0442\u0430 \u0441\u0440\u0435\u0434\u0430." id="yQUlKUtfYB7Y"
# ## Библиотеки и технологии, които смятаме да използваме
#
# Проектът ще бъде реализиран на **Python** с **Jupyter Notebook**, като ще използваме основни библиотеки от екосистемата за работа с таблични данни и `scikit-learn`:
#
# - **NumPy** – числови операции и масиви;
# - **Pandas** – зареждане и обработка на данните (`CSV`), филтриране, трансформации;
# - **Matplotlib** и **Seaborn** – визуализации за EDA и представяне на резултатите;
# - **Scikit-learn** – основната библиотека за целия ML pipeline:
#   - предварителна обработка: `StandardScaler` / `MinMaxScaler`, `LabelEncoder` / `OneHotEncoder` (ако е нужно),
#   - модели: Logistic Regression, kNN, SVM, Decision Tree / Random Forest, KMeans, DBSCAN (и евентуално Agglomerative),
#   - оценка: метрики за класификация и клъстеризация,
#   - валидация и tuning: `train_test_split`, `cross_val_score`, `GridSearchCV` / `RandomizedSearchCV`,
#   - **Pipeline** и **ColumnTransformer** (за по-чист и възпроизводим код);
# - *(ако е нужно за статистическа част като при preliminary analysis)* **Statsmodels** – за допълнителни статистически тестове и проверки;
# - **kagglehub** – за изтегляне на набора от данни от Kaggle в работната среда.

# %% [markdown] cell_id="77592aa4510e4f6e9751c1531116a45b" deepnote_block_group="009a9d14cba44937acad976795bbd4d7" deepnote_cell_type="markdown" deepnote_sorting_key="42" deepnote_source="# \u0427\u0430\u0441\u0442 1: \u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u2013 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\n\n\u0412 \u043f\u044a\u0440\u0432\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u043e **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f**, \u043f\u0440\u0438 \u043a\u043e\u044f\u0442\u043e \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u0436\u0430\u043d\u0440\u044a\u0442 (`track_genre`) \u043d\u0430 \u0434\u0430\u0434\u0435\u043d\u0430 \u043f\u0435\u0441\u0435\u043d \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043a\u0430\u0442\u043e *danceability, energy, acousticness, valence* \u0438 \u0434\u0440.  \n\u0426\u0435\u043b\u0442\u0430 \u0435 \u0434\u0430 \u0441\u0435 \u0441\u0440\u0430\u0432\u043d\u044f\u0442 \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u043a\u043e\u0438 \u043e\u0442 \u0442\u044f\u0445 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0435 \u0437\u0430 \u0442\u0430\u0437\u0438 \u0437\u0430\u0434\u0430\u0447\u0430.\n" id="qdO1HPJtYB7Y"
# # Част 1: Класификационна задача – предсказване на жанр
#
# В първата част се разглежда задача по **класификация**, при която се предсказва жанрът (`track_genre`) на дадена песен на база числови аудио признаци като *danceability, energy, acousticness, valence* и др.  
# Целта е да се сравнят класически алгоритми за класификация и да се оцени кои от тях се справят най-добре за тази задача.
#

# %% [markdown] cell_id="dfbc1df9dbf0465e99cada405b2926d0" deepnote_block_group="620684948d48433fb4cd2c223ad9f403" deepnote_cell_type="markdown" deepnote_sorting_key="43" deepnote_source="## \u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (\u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f)\n\n\u041f\u0440\u0435\u0434\u0438 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435\u0442\u043e \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438 \u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0434\u0430 \u0441\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u0432\u044f\u0442 \u0442\u0430\u043a\u0430, \u0447\u0435 \u0434\u0430 \u0441\u0430 \u043a\u043e\u0440\u0435\u043a\u0442\u043d\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438 \u0437\u0430 ML \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438:\n\n- **\u041f\u043e\u0447\u0438\u0441\u0442\u0432\u0430\u043d\u0435**: \u043f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u0434\u0443\u0431\u043b\u0438\u0440\u0430\u043d\u0438 \u0437\u0430\u043f\u0438\u0441\u0438 \u0438 \u0440\u0435\u0434\u043e\u0432\u0435 \u0441 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0438\u043b\u0438 \u0437\u0430\u043f\u044a\u043b\u0432\u0430\u043d\u0435 \u043f\u0440\u0438 \u043d\u0443\u0436\u0434\u0430)\n- **\u0422\u0438\u043f\u043e\u0432\u0435 \u0434\u0430\u043d\u043d\u0438**: \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0432\u0430 \u0441\u0435 \u0442\u0438\u043f\u044a\u0442 \u043d\u0430 \u043a\u043e\u043b\u043e\u043d\u0438\u0442\u0435 \u0438 \u043f\u0440\u0438 \u043d\u0443\u0436\u0434\u0430 \u0441\u0435 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u0443\u0432\u0430\u0442 \u0432 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\n- **\u0418\u0437\u0431\u043e\u0440 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 (features)**: \u0432 \u043c\u043e\u0434\u0435\u043b\u0430 \u0441\u0435 \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0442 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430, \u043d\u0430\u043f\u0440. danceability, energy, loudness) \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d \u0431\u0440\u043e\u0439 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 (\u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043a\u043e\u043b\u043e\u043d\u0438, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0430 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430, \u043d\u0430\u043f\u0440. popularity, duration_ms). \u0422\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u043f\u043e\u043b\u0435\u0442\u0430 (\u043d\u0430\u043f\u0440. \u0438\u043c\u0435 \u043d\u0430 \u043f\u0435\u0441\u0435\u043d/\u0438\u0437\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b) \u043d\u0435 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0438\u0437\u0438\u0441\u043a\u0432\u0430\u0442 \u043e\u0442\u0434\u0435\u043b\u0435\u043d \u043f\u043e\u0434\u0445\u043e\u0434 \u0437\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0442\u0435\u043a\u0441\u0442.\n- **\u0420\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 train/test**: \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435\u0442\u043e \u0435 \u0441\u0442\u0440\u0430\u0442\u0438\u0444\u0438\u0446\u0438\u0440\u0430\u043d\u043e \u043f\u043e track_genre, \u0442\u0430\u043a\u0430 \u0447\u0435 \u0432\u0441\u0435\u043a\u0438 \u0436\u0430\u043d\u0440 \u0434\u0430 \u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0435\u043d \u0441\u0445\u043e\u0434\u043d\u043e \u0432 \u043e\u0431\u0443\u0447\u0430\u0432\u0430\u0449\u0438\u044f \u0438 \u0442\u0435\u0441\u0442\u043e\u0432\u0438\u044f \u043d\u0430\u0431\u043e\u0440\n- **\u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f (scaling)**: \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u0441\u0435 `StandardScaler`, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0447\u0430\u0441\u0442 \u043e\u0442 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 (\u043d\u0430\u043f\u0440. Logistic Regression, kNN, SVM) \u0441\u0430 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u043d\u0438 \u043a\u044a\u043c \u043c\u0430\u0449\u0430\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435. \u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 `Pipeline`, \u0437\u0430 \u0434\u0430 \u0441\u0435 \u0438\u0437\u0431\u0435\u0433\u043d\u0435 data leakage (scaler \u0441\u0435 \u043e\u0431\u0443\u0447\u0430\u0432\u0430 \u0441\u0430\u043c\u043e \u0432\u044a\u0440\u0445\u0443 train \u0447\u0430\u0441\u0442\u0442\u0430)\n\n**\u0420\u0430\u0437\u043b\u0438\u043a\u0430 \u0441\u043f\u0440\u044f\u043c\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430:** \u043f\u0440\u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u044f\u043c\u0430 \u0446\u0435\u043b\u0435\u0432\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0438 \u043d\u044f\u043c\u0430 train/test split \u0432 \u0441\u044a\u0449\u0438\u044f \u0441\u043c\u0438\u0441\u044a\u043b; scaling \u0435 \u043e\u0449\u0435 \u043f\u043e-\u0432\u0430\u0436\u0435\u043d, \u0437\u0430\u0449\u043e\u0442\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435 \u0441\u0430 distance-based; \u0437\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u0441\u0435 \u043f\u043e\u0434\u0431\u0438\u0440\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u043d\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438, \u0441\u0432\u044a\u0440\u0437\u0430\u043d\u0438 \u0441\u044a\u0441 \u0437\u0432\u0443\u0447\u0435\u043d\u0435 \u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435, \u0432\u043c\u0435\u0441\u0442\u043e \u0432\u0441\u0438\u0447\u043a\u0438 \u043d\u0430\u043b\u0438\u0447\u043d\u0438 \u043a\u043e\u043b\u043e\u043d\u0438.\n" id="9lSnhdg7YB7Y"
# ## Предварителна обработка на данните (за класификация)
#
# Преди обучението на модели е необходимо данните да се подготвят така, че да са коректни и подходящи за ML алгоритми:
#
# - **Почистване**: премахване на дублирани записи и редове с липсващи стойности (или запълване при нужда)
# - **Типове данни**: проверява се типът на колоните и при нужда се преобразуват в числови стойности
# - **Избор на признаци (features)**: в модела се включват само числови аудио характеристики (извлечени директно от аудио сигнала, напр. danceability, energy, loudness) и ограничен брой допълнителни числови атрибути (числови колони, които не са извлечени от аудио сигнала, напр. popularity, duration_ms). Текстови полета (напр. име на песен/изпълнител) не се използват, тъй като изискват отделен подход за обработка на текст.
# - **Разделяне train/test**: разделянето е стратифицирано по track_genre, така че всеки жанр да е представен сходно в обучаващия и тестовия набор
# - **Нормализация (scaling)**: прилага се `StandardScaler`, тъй като част от моделите (напр. Logistic Regression, kNN, SVM) са чувствителни към мащаба на признаците. Използва се `Pipeline`, за да се избегне data leakage (scaler се обучава само върху train частта)
#
# **Разлика спрямо клъстеризацията:** при клъстеризация няма целева променлива и няма train/test split в същия смисъл; scaling е още по-важен, защото алгоритмите са distance-based; за клъстеризацията се подбират основно признаци, свързани със звучене и настроение, вместо всички налични колони.
#

# %% cell_id="1f2ce432efe540e2a6ada68c11b3e228" deepnote_block_group="636ac9ebc27b4152a9e5e156f8754ecc" deepnote_cell_type="code" deepnote_content_hash="c085b6ba" deepnote_execution_finished_at="2026-01-27T20:26:37.212Z" deepnote_execution_started_at="2026-01-27T20:26:37.211Z" deepnote_sorting_key="44" deepnote_source="df.head()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1 execution_start=1769545597211 id="uCj_tRW3YB7Y" outputId="465639b7-485a-4e08-d7d2-43f26297d0e4" source_hash="c085b6ba"
df.head()

# %% cell_id="9491e29799d0492ea3cc4c36171a4946" colab={"base_uri": "https://localhost:8080/"} deepnote_block_group="5bed78181ff440708e16d2a98e89a69a" deepnote_cell_type="code" deepnote_content_hash="20c58c7b" deepnote_execution_finished_at="2026-01-27T21:47:25.112Z" deepnote_execution_started_at="2026-01-27T21:47:24.981Z" deepnote_sorting_key="45" deepnote_source="df_cls = df.copy()\n\n# \u041f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u044a\u043b\u043d\u0438 \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u0438\ndf_cls = df_cls.drop_duplicates()\n\n# \u041f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u0440\u0435\u0434\u043e\u0432\u0435 \u0441 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0432 \u0442\u043e\u0437\u0438 dataset \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0441\u0430 \u043c\u043d\u043e\u0433\u043e \u043c\u0430\u043b\u043a\u043e)\ndf_cls = df_cls.dropna()\n\n# explicit \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u0443\u0432\u0430\u043c\u0435 \u043a\u044a\u043c 0/1 (int)\nif \"explicit\" in df_cls.columns:\n    df_cls[\"explicit\"] = df_cls[\"explicit\"].astype(int)\n\ndf_cls.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=131 execution_start=1769550444981 id="7R0iwlFDYB7Y" outputId="749bd274-c46d-40b6-c7f0-cfdbe8eed96b" source_hash="20c58c7b"
df_cls = df.copy()

# Премахване на пълни дубликати
df_cls = df_cls.drop_duplicates()

# Премахване на редове с липсващи стойности (в този dataset обикновено са много малко)
df_cls = df_cls.dropna()

# explicit преобразуваме към 0/1 (int)
if "explicit" in df_cls.columns:
    df_cls["explicit"] = df_cls["explicit"].astype(int)

df_cls.shape

# %% cell_id="135b2534d65449b6a51cf11f3e91a374" colab={"base_uri": "https://localhost:8080/", "height": 206} deepnote_block_group="1ac4a0fba2924737a181b67330104066" deepnote_cell_type="code" deepnote_content_hash="b4e731c" deepnote_execution_finished_at="2026-01-27T21:47:27.568Z" deepnote_execution_started_at="2026-01-27T21:47:27.524Z" deepnote_sorting_key="46" deepnote_source="target_col = \"track_genre\"\n\n# \u0417\u0430 features \u0438\u043c\u0430\u043c\u0435 \u0434\u0432\u0430 \u0442\u0438\u043f\u0430: \n# A\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043e\u043f\u0438\u0441\u0432\u0430\u0442 \u0437\u0432\u0443\u0447\u0435\u043d\u0435/\u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435) - \u043d\u0430\u043f\u0440. danceability, energy, loudness, speechiness, acousticness\n# \u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 (\u043d\u0435 \u0441\u0430 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430) - \u043d\u0430\u043f\u0440. popularity, duration_ms, explicit\n# \u041c\u0430\u0445\u0430\u043c\u0435 id, \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u043f\u043e\u043b\u0435\u0442\u0430 \u0438 key_name (\u0434\u0443\u0431\u043b\u0438\u0440\u0430 key, \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435)\ndrop_cols = [\n    \"track_id\", \"artists\", \"album_name\", \"track_name\", \"key_name\"\n]\n\nfeature_cols = [c for c in df.columns if c not in drop_cols + [target_col]]\nfeature_cols\n\ndf_cls = df_cls[feature_cols + [target_col]].copy()\n\ndf_cls.head()" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=44 execution_start=1769550447524 id="LAuUtpMEYB7Y" outputId="6d9db448-3c1c-4d8d-c2d4-07aa7b7fa123" source_hash="b4e731c"
target_col = "track_genre"

# За features имаме два типа:
# Aудио характеристики (описват звучене/настроение) - напр. danceability, energy, loudness, speechiness, acousticness
# Допълнителни числови атрибути (не са директно от аудио сигнала) - напр. popularity, duration_ms, explicit
# Махаме id, текстови полета и key_name (дублира key, текстово представяне)
drop_cols = [
    "track_id", "artists", "album_name", "track_name", "key_name"
]

feature_cols = [c for c in df.columns if c not in drop_cols + [target_col]]
feature_cols

df_cls = df_cls[feature_cols + [target_col]].copy()

df_cls.head()

# %% cell_id="3660c1bb0d074bb8a881d7a055336e87" colab={"base_uri": "https://localhost:8080/"} deepnote_block_group="d9c3364dd18348eab5f57b2d14b5cee7" deepnote_cell_type="code" deepnote_content_hash="2e3daa39" deepnote_execution_finished_at="2026-01-27T21:47:29.981Z" deepnote_execution_started_at="2026-01-27T21:47:29.911Z" deepnote_sorting_key="47" deepnote_source="# Train/test split \u0441\u044a\u0441 \u0441\u0442\u0440\u0430\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f\nX = df_cls[feature_cols]\ny = df_cls[target_col]\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y,\n    test_size=0.2,\n    random_state=67,\n    stratify=y\n)\n\nX_train.shape, X_test.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=70 execution_start=1769550449911 id="zRxwFiCFYB7Z" outputId="54f21fa5-7ad9-4b2d-c943-7765ada8b071" source_hash="2e3daa39"
# Train/test split със стратификация
X = df_cls[feature_cols]
y = df_cls[target_col]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=67,
    stratify=y
)

X_train.shape, X_test.shape

# %% cell_id="e9daa02d06fd4ae5bd38c902b26bee9c" colab={"base_uri": "https://localhost:8080/", "height": 149} deepnote_block_group="2b39457c78d047b0bac78b9016db326d" deepnote_cell_type="code" deepnote_content_hash="288c6149" deepnote_execution_finished_at="2026-01-27T21:47:33.063Z" deepnote_execution_started_at="2026-01-27T21:47:33.058Z" deepnote_sorting_key="48" deepnote_source="# \u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f (scaling)\n\n# ColumnTransformer \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0432\u044a\u0440\u0445\u0443 \u0433\u0440\u0443\u043f\u0438 \u043a\u043e\u043b\u043e\u043d\u0438 (\u0442\u0443\u043a: \u0432\u044a\u0440\u0445\u0443 feature_cols)\n# \"num\" \u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u044a\u0442 \u043d\u0430 \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f\u0442\u0430 \u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\npreprocess_cls = ColumnTransformer(\n    transformers=[\n        (\"num\", StandardScaler(), feature_cols)\n    ],\n    remainder=\"drop\" # \u0412\u0441\u0438\u0447\u043a\u0438 \u043a\u043e\u043b\u043e\u043d\u0438, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0430 \u0432 feature_cols, \u0441\u0435 \u043f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u0442\n)\n\npreprocess_cls" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=5 execution_start=1769550453058 id="w1VKwxgAYB7Z" outputId="f309fb88-b04a-4815-bb31-8bbe0adcc816" source_hash="288c6149"
# Нормализация (scaling)

# ColumnTransformer прилага трансформации върху групи колони (тук: върху feature_cols)
# "num" е етикетът на трансформацията за числовите признаци
preprocess_cls = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), feature_cols)
    ],
    remainder="drop" # Всички колони, които не са в feature_cols, се премахват
)

preprocess_cls

# %% cell_id="bb08665690ae4df286af102943dafba5" colab={"base_uri": "https://localhost:8080/"} deepnote_block_group="8ce98f1aa606430d8b05e62221643241" deepnote_cell_type="code" deepnote_content_hash="e5e4d9b6" deepnote_execution_finished_at="2026-01-27T21:47:37.245Z" deepnote_execution_started_at="2026-01-27T21:47:37.210Z" deepnote_sorting_key="49" deepnote_source="# \u041f\u0440\u0438\u043b\u0430\u0433\u0430\u043d\u0435 \u043d\u0430 \u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430\nX_train_scaled = preprocess_cls.fit_transform(X_train)\nX_test_scaled = preprocess_cls.transform(X_test)\n\nX_train_scaled.shape, X_test_scaled.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=35 execution_start=1769550457210 id="YuXaCafHYB7Z" outputId="bc4feb04-5ec2-4889-8f15-02bd7f523e41" source_hash="e5e4d9b6"
# Прилагане на нормализацията
X_train_scaled = preprocess_cls.fit_transform(X_train)
X_test_scaled = preprocess_cls.transform(X_test)

X_train_scaled.shape, X_test_scaled.shape

# %% [markdown] cell_id="837b588f61df4fd2b7fac1669bfd358a" deepnote_block_group="6a49fce0cee44b43ac1ff6690f7ffec2" deepnote_cell_type="markdown" deepnote_sorting_key="50" deepnote_source="## \u041c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f)\n\n\u0412 \u0442\u0430\u0437\u0438 \u0441\u0435\u043a\u0446\u0438\u044f \u0441\u0435 \u043e\u0431\u0443\u0447\u0430\u0432\u0430\u0442 \u0438 \u0441\u0440\u0430\u0432\u043d\u044f\u0432\u0430\u0442 \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u044a\u043c\u0430 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 `track_genre` \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438.  \n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 \u0435\u0434\u0438\u043d \u0438 \u0441\u044a\u0449 preprocessing pipeline (\u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u044a\u0441 `StandardScaler`), \u0437\u0430 \u0434\u0430 \u0441\u0430 \u043a\u043e\u0440\u0435\u043a\u0442\u043d\u0438 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f\u0442\u0430.  \n\u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0441\u0435 \u043e\u0446\u0435\u043d\u044f\u0432\u0430\u0442 \u043a\u0430\u043a\u0442\u043e \u043d\u0430 \u0442\u0435\u0441\u0442\u043e\u0432 \u043d\u0430\u0431\u043e\u0440, \u0442\u0430\u043a\u0430 \u0438 \u0447\u0440\u0435\u0437 cross-validation. \u0417\u0430 \u0447\u0430\u0441\u0442 \u043e\u0442 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 \u0441\u0435 \u043f\u0440\u0430\u0432\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0447\u0440\u0435\u0437 `GridSearchCV`.\n" id="0la9o7-8YB7Z"
# ## Моделиране на данните (класификация)
#
# В тази секция се обучават и сравняват няколко класически алгоритъма за класификация на `track_genre` на база числови аудио характеристики.  
# Използва се един и същ preprocessing pipeline (нормализация със `StandardScaler`), за да са коректни сравненията.  
# Резултатите се оценяват както на тестов набор, така и чрез cross-validation. За част от моделите се прави настройка на хиперпараметри чрез `GridSearchCV`.
#

# %% cell_id="6d444fef01a746c98565ab1363e1914e" deepnote_block_group="30ada9136e4e46a4a05c2289d56651a1" deepnote_cell_type="code" deepnote_content_hash="eee912e0" deepnote_execution_finished_at="2026-01-27T21:24:44.449Z" deepnote_execution_started_at="2026-01-27T21:24:44.447Z" deepnote_sorting_key="51" deepnote_source="print(\"\u041e\u0431\u0449 \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435:\", df[\"track_genre\"].nunique())" execution_context_id="4c6b5e76-66bb-4d77-99bd-b33de1734382" execution_millis=2 execution_start=1769549084447 id="Bgxd19DrYB7Z" outputId="0cedd53c-bb0a-4859-91e8-cfb9efb2f606" source_hash="eee912e0"
print("Общ брой жанрове:", df["track_genre"].nunique())

# %% [markdown] cell_id="209916747cdd40b1bcc11cb7b8557c6e" deepnote_block_group="8abac77f0d9548c3ab379129abff5a0f" deepnote_cell_type="markdown" deepnote_sorting_key="52" deepnote_source="### \u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0438\u0437\u0431\u043e\u0440\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 (feature selection)\n\n\u0421 \u0446\u0435\u043b \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u0432\u043b\u0438\u044f\u043d\u0438\u0435\u0442\u043e \u043d\u0430 \u0438\u0437\u0431\u043e\u0440\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0432\u044a\u0440\u0445\u0443 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f\u0442\u0430, \u0431\u044f\u0445\u0430 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438 \u0442\u0440\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 features:  \n(1) \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043e\u0442 \u043d\u0430\u0439-\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u043f\u043e\u0440\u0435\u0434 EDA,  \n(2) \u0441\u044a\u0449\u043e\u0442\u043e \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0441 \u0434\u043e\u0431\u0430\u0432\u0435\u043d\u043e \u0442\u0435\u043c\u043f\u043e (`tempo`),  \n(3) \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u0432\u0441\u0438\u0447\u043a\u0438 \u043d\u0430\u043b\u0438\u0447\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438.\n\n\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435\u0442\u043e \u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u0435\u043d\u043e \u0447\u0440\u0435\u0437 cross-validation \u0441 Logistic Regression \u0438 \u043c\u0435\u0442\u0440\u0438\u043a\u0430 **Macro F1**, \u043a\u043e\u044f\u0442\u043e \u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0430 \u0437\u0430 \u043c\u043d\u043e\u0433\u043e-\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f.\n\n\u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0441 \u043f\u044a\u043b\u043d\u0438\u044f \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e-\u0432\u0438\u0441\u043e\u043a Macro F1 \u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0449\u0438 \u0441\u0430\u043c\u043e \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u0438\u0442\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0441\u043f\u043e\u0440\u0435\u0434 EDA. \u0422\u043e\u0432\u0430 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 \u0434\u043e\u043f\u0440\u0438\u043d\u0430\u0441\u044f\u0442 \u0437\u0430 \u043f\u043e-\u0434\u043e\u0431\u0440\u043e \u0440\u0430\u0437\u0433\u0440\u0430\u043d\u0438\u0447\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n\n\u0412 \u0441\u043b\u0435\u0434\u0432\u0430\u0449\u0438\u0442\u0435 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0438 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 features.\n" id="y1dRT2K2YB7Z"
# ### Анализ на избора на признаци (feature selection)
#
# С цел да се оцени влиянието на избора на признаци върху качеството на класификацията, бяха сравнени три различни набора от features:  
# (1) подмножество от най-информативните аудио характеристики според EDA,  
# (2) същото подмножество с добавено темпо (`tempo`),  
# (3) пълният набор от всички налични числови признаци.
#
# Сравнението е направено чрез cross-validation с Logistic Regression и метрика **Macro F1**, която е подходяща за много-класова класификация.
#
# Резултатите показват, че моделът с пълния набор от признаци постига значително по-висок Macro F1 в сравнение с моделите, използващи само най-силните признаци според EDA. Това показва, че допълнителните числови атрибути допринасят за по-добро разграничаване на жанровете.
#
# В следващите експерименти се използва пълният набор от features.
#

# %% cell_id="68be52c289094b74ad75e89811229517" deepnote_block_group="eec6ace5cc844f078d0b397b3c25eba6" deepnote_cell_type="code" deepnote_content_hash="9d3207c4" deepnote_execution_finished_at="2026-01-27T20:26:37.771Z" deepnote_execution_started_at="2026-01-27T20:26:37.771Z" deepnote_sorting_key="53" deepnote_source="# Feature set 1: \u0442\u043e\u043f \u0441\u043f\u043e\u0440\u0435\u0434 EDA\nfeatures_eda_top = [\n    \"acousticness\",\"energy\",\"instrumentalness\",\"loudness\",\n    \"speechiness\",\"danceability\",\"valence\",\"liveness\"\n]\n\n# Feature set 2: + tempo\nfeatures_eda_top_plus = features_eda_top + [\"tempo\"]\n\n# Feature set 3: \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440\nfeatures_full = feature_cols  # \u043e\u0442 \u0442\u0432\u043e\u044f preprocessing" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545597771 id="PNuG-LRVYB7a" source_hash="9d3207c4"
# Feature set 1: топ според EDA
features_eda_top = [
    "acousticness","energy","instrumentalness","loudness",
    "speechiness","danceability","valence","liveness"
]

# Feature set 2: + tempo
features_eda_top_plus = features_eda_top + ["tempo"]

# Feature set 3: пълният набор
features_full = feature_cols  # от твоя preprocessing


# %% cell_id="60f098e4e9154742b5e08806813f2e1b" deepnote_block_group="6c74508e25d04149906459595b74c454" deepnote_cell_type="code" deepnote_content_hash="5f47b7cf" deepnote_execution_finished_at="2026-01-27T20:30:24.261Z" deepnote_execution_started_at="2026-01-27T20:26:37.831Z" deepnote_sorting_key="54" deepnote_source="def cv_macro_f1(df, features, target=\"track_genre\", cv=3):\n    X = df[features]\n    y = df[target]\n\n    model = Pipeline([\n        (\"scale\", StandardScaler()),\n        (\"clf\", LogisticRegression(max_iter=2000))\n    ])\n\n    scores = cross_val_score(model, X, y, scoring=\"f1_macro\", cv=cv, n_jobs=-1)\n    return scores.mean(), scores.std()\n\n\nfeature_sets = {\n    \"EDA top\": features_eda_top,\n    \"EDA top + tempo\": features_eda_top_plus,\n    \"Full features\": feature_cols\n}\n\nfor name, feats in feature_sets.items():\n    mean_f1, std_f1 = cv_macro_f1(df, feats)\n    print(f\"{name:15s} -> Macro F1: {mean_f1:.4f} \u00b1 {std_f1:.4f}\")" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=226430 execution_start=1769545597831 id="NLSB7rPJYB7a" outputId="cd384d27-068d-4689-9c48-0610fb9e4097" source_hash="5f47b7cf"
def cv_macro_f1(df, features, target="track_genre", cv=3):
    X = df[features]
    y = df[target]

    model = Pipeline([
        ("scale", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000))
    ])

    scores = cross_val_score(model, X, y, scoring="f1_macro", cv=cv, n_jobs=-1)
    return scores.mean(), scores.std()


feature_sets = {
    "EDA top": features_eda_top,
    "EDA top + tempo": features_eda_top_plus,
    "Full features": feature_cols
}

for name, feats in feature_sets.items():
    mean_f1, std_f1 = cv_macro_f1(df, feats)
    print(f"{name:15s} -> Macro F1: {mean_f1:.4f} ± {std_f1:.4f}")


# %% [markdown] cell_id="ff8dff9d286f493bbafc07be58f81092" deepnote_block_group="97ca620f3e224923aa5a79985ead4cf1" deepnote_cell_type="markdown" deepnote_sorting_key="55" deepnote_source="### \u041e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435\n\n\u0417\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0438\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u0435 \u0434\u0435\u0444\u0438\u043d\u0438\u0440\u0430\u043d\u0430 \u043e\u0431\u0449\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f, \u043a\u043e\u044f\u0442\u043e \u0438\u0437\u0432\u044a\u0440\u0448\u0432\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435, \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435 \u0438 \u0438\u0437\u0447\u0438\u0441\u043b\u044f\u0432\u0430\u043d\u0435 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u0438\u0442\u0435 \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e.  \n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442 \u0441\u0435 **Accuracy** \u0438 **Macro F1**, \u043a\u0430\u0442\u043e Macro F1 \u0435 \u0432\u043e\u0434\u0435\u0449\u0430\u0442\u0430 \u043c\u0435\u0442\u0440\u0438\u043a\u0430 \u043f\u043e\u0440\u0430\u0434\u0438 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0438\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440 \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430.\n\n\u0424\u0443\u043d\u043a\u0446\u0438\u044f\u0442\u0430 \u0438\u0437\u0432\u0435\u0436\u0434\u0430 \u0438 **classification report** \u0441 Precision, Recall \u0438 F1-score \u0437\u0430 \u0432\u0441\u0435\u043a\u0438 \u0436\u0430\u043d\u0440, \u043a\u0430\u043a\u0442\u043e \u0438 **confusion matrix** \u0437\u0430 \u043d\u0430\u0439-\u0447\u0435\u0441\u0442\u043e \u0441\u0440\u0435\u0449\u0430\u043d\u0438\u0442\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438\u0442\u0435 \u0433\u0440\u0435\u0448\u043a\u0438 \u0438 \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435.\n" id="ZaHLxWliYB7a"
# ### Оценка на моделите
#
# За оценка на класификационните модели е дефинирана обща функция, която извършва обучение, предсказване и изчисляване на основните метрики за качество.  
# Използват се **Accuracy** и **Macro F1**, като Macro F1 е водещата метрика поради многокласовия характер на задачата.
#
# Функцията извежда и **classification report** с Precision, Recall и F1-score за всеки жанр, както и **confusion matrix** за най-често срещаните жанрове, което позволява анализ на типичните грешки и припокривания между класовете.
#

# %% cell_id="0b66e4b3545a4d55b451f9c7284d796b" deepnote_block_group="af246d9e01ce4576b42f8c9385fdfa74" deepnote_cell_type="code" deepnote_content_hash="b844fba7" deepnote_execution_finished_at="2026-01-27T21:47:44.431Z" deepnote_execution_started_at="2026-01-27T21:47:44.431Z" deepnote_sorting_key="56" deepnote_source="def evaluate_classifier(\n    model_pipeline: Pipeline,\n    X_train,\n    y_train,\n    X_test,\n    y_test,\n    top_n: int = 10,\n    show_confusion: bool = True,\n    print_report: bool = True\n):\n    # \u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u0438 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435\n    model_pipeline.fit(X_train, y_train)\n    y_pred = model_pipeline.predict(X_test)\n\n    # \u041e\u0441\u043d\u043e\u0432\u043d\u0438 \u043c\u0435\u0442\u0440\u0438\u043a\u0438 - \u0438\u0437\u0431\u0440\u0430\u043b\u0438 \u0441\u043c\u0435 accuracy \u0438 macro f1\n    acc = accuracy_score(y_test, y_pred)\n    macro_f1 = f1_score(y_test, y_pred, average=\"macro\")\n\n    print(f\"Accuracy: {acc:.4f}\")\n    print(f\"Macro F1: {macro_f1:.4f}\")\n\n    # Classification report (precision/recall/F1 \u043f\u043e \u043a\u043b\u0430\u0441 + macro/weighted)\n    if print_report:\n        print(\"\\nClassification report:\")\n        print(classification_report(y_test, y_pred))\n\n    # Confusion matrix \u0437\u0430 top-N \u0436\u0430\u043d\u0440\u0430\n    if show_confusion:\n        top_genres = y_test.value_counts().head(top_n).index\n\n        mask = y_test.isin(top_genres)\n        y_test_top = y_test[mask]\n\n        y_pred_series = pd.Series(y_pred, index=y_test.index)\n        y_pred_top = y_pred_series[mask]\n\n        cm = confusion_matrix(y_test_top, y_pred_top, labels=top_genres)\n\n        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=top_genres)\n        plt.figure(figsize=(10, 8))\n        disp.plot(include_values=True, xticks_rotation=45)\n        plt.title(f\"Confusion Matrix (Top {top_n} \u0436\u0430\u043d\u0440\u0430)\")\n        plt.tight_layout()\n        plt.show()\n\n    return {\n        \"accuracy\": acc,\n        \"macro_f1\": macro_f1\n    }" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=0 execution_start=1769550464431 id="PTTzNWBcYB7a" source_hash="b844fba7"
def evaluate_classifier(
    model_pipeline: Pipeline,
    X_train,
    y_train,
    X_test,
    y_test,
    top_n: int = 10,
    show_confusion: bool = True,
    print_report: bool = True
):
    # Обучение и предсказване
    model_pipeline.fit(X_train, y_train)
    y_pred = model_pipeline.predict(X_test)

    # Основни метрики - избрали сме accuracy и macro f1
    acc = accuracy_score(y_test, y_pred)
    macro_f1 = f1_score(y_test, y_pred, average="macro")

    print(f"Accuracy: {acc:.4f}")
    print(f"Macro F1: {macro_f1:.4f}")

    # Classification report (precision/recall/F1 по клас + macro/weighted)
    if print_report:
        print("\nClassification report:")
        print(classification_report(y_test, y_pred))

    # Confusion matrix за top-N жанра
    if show_confusion:
        top_genres = y_test.value_counts().head(top_n).index

        mask = y_test.isin(top_genres)
        y_test_top = y_test[mask]

        y_pred_series = pd.Series(y_pred, index=y_test.index)
        y_pred_top = y_pred_series[mask]

        cm = confusion_matrix(y_test_top, y_pred_top, labels=top_genres)

        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=top_genres)
        plt.figure(figsize=(10, 8))
        disp.plot(include_values=True, xticks_rotation=45)
        plt.title(f"Confusion Matrix (Top {top_n} жанра)")
        plt.tight_layout()
        plt.show()

    return {
        "accuracy": acc,
        "macro_f1": macro_f1
    }


# %% [markdown] cell_id="010ef125255b412cb15224c1573d852c" deepnote_block_group="8c6ba168c01b4a839774487be8fde965" deepnote_cell_type="markdown" deepnote_sorting_key="57" deepnote_source="### Logistic Regression (baseline)\n\n\u041b\u0438\u043d\u0435\u0435\u043d \u043c\u043e\u0434\u0435\u043b, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d \u043a\u0430\u0442\u043e \u0431\u0430\u0437\u0430 \u0437\u0430 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435. \u041f\u043e\u0434\u0445\u043e\u0434\u044f\u0449 \u0437\u0430 \u0431\u044a\u0440\u0437\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u0442\u043e\u0432\u0430\n\u0434\u043e\u043a\u043e\u043b\u043a\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0441\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u0438 \u0432 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435.\n" id="WTfOYAeCYB7a"
# ### Logistic Regression (baseline)
#
# Линеен модел, използван като база за сравнение. Подходящ за бърза оценка на това
# доколко жанровете са линейно разделими в пространството на признаците.
#

# %% cell_id="d4d24f3f3a944ae9869f9cfdc2c0fbac" deepnote_block_group="b0efb22a5f024bfdaf6ebe35cc45491a" deepnote_cell_type="code" deepnote_content_hash="9d2705f5" deepnote_execution_finished_at="2026-01-27T20:37:14.098Z" deepnote_execution_started_at="2026-01-27T20:35:56.161Z" deepnote_sorting_key="58" deepnote_source="logreg_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", LogisticRegression(max_iter=3000))\n])\n\nlogreg_results = evaluate_classifier(\n    model_pipeline=logreg_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=True,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=77937 execution_start=1769546156161 id="5CKL7R_CYB7a" outputId="b0e0d9c6-df90-4518-c989-88e9fc439e2b" source_hash="9d2705f5"
logreg_model = Pipeline(steps=[
    ("prep", preprocess_cls),
    ("model", LogisticRegression(max_iter=3000))
])

logreg_results = evaluate_classifier(
    model_pipeline=logreg_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=True,
    print_report=False
)

# %% [markdown] cell_id="3fff7fe97b2d4d6d90f192ad3cf2b76d" deepnote_block_group="f3365c1a3cf54d4fa137fa3031ae9895" deepnote_cell_type="markdown" deepnote_sorting_key="59" deepnote_source="### k-Nearest Neighbors (kNN)\n\nkNN \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u0446\u0438\u0440\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u043d\u0430 \u0431\u0430\u0437\u0430 \u0441\u0445\u043e\u0434\u0441\u0442\u0432\u043e\u0442\u043e \u0438\u043c \u0441 \u043d\u0430\u0439-\u0431\u043b\u0438\u0437\u043a\u0438\u0442\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u0438 \u0432 feature \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e\u0442\u043e.\n\u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0435 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a\u044a\u043c \u043c\u0430\u0449\u0430\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435, \u043f\u043e\u0440\u0430\u0434\u0438 \u043a\u043e\u0435\u0442\u043e \u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0430.\n" id="_07NkLzwYB7b"
# ### k-Nearest Neighbors (kNN)
#
# kNN класифицира песните на база сходството им с най-близките примери в feature пространството.
# Моделът е чувствителен към мащаба на признаците, поради което нормализацията е необходима.
#

# %% cell_id="e9425d3c19e24517807c7cdeb713b03e" deepnote_block_group="7c973ad9c1d7434abe8c4f5f1efc0bb7" deepnote_cell_type="code" deepnote_content_hash="a4571e0f" deepnote_execution_finished_at="2026-01-27T20:39:25.099Z" deepnote_execution_started_at="2026-01-27T20:38:36.271Z" deepnote_sorting_key="60" deepnote_source="knn_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", KNeighborsClassifier(n_neighbors=15))\n])\n\nknn_results = evaluate_classifier(\n    model_pipeline=knn_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=48828 execution_start=1769546316271 id="8nkjQj1rYB7b" outputId="dcbca53d-8e34-482d-95d2-6c4ef81404c2" source_hash="a4571e0f"
knn_model = Pipeline(steps=[
    ("prep", preprocess_cls),
    ("model", KNeighborsClassifier(n_neighbors=15))
])

knn_results = evaluate_classifier(
    model_pipeline=knn_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=False,
    print_report=False
)

# %% [markdown] cell_id="830e41d2b0da422abecd892cfd7a010e" deepnote_block_group="2af4bc24623a45bb85a2fcf85d198a74" deepnote_cell_type="markdown" deepnote_sorting_key="61" deepnote_source="#### \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u043d\u0430 kNN\n\n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 GridSearchCV \u0437\u0430 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u0435\u043d \u0431\u0440\u043e\u0439 \u0441\u044a\u0441\u0435\u0434\u0438 \u0438 \u043d\u0430\u0447\u0438\u043d \u043d\u0430 \u043f\u0440\u0435\u0442\u0435\u0433\u043b\u044f\u043d\u0435,\n\u043a\u0430\u0442\u043e \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0437\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u0435 Macro F1.\n" id="RjbxlxuvYB7b"
# #### Настройка на хиперпараметрите на kNN
#
# Използва се GridSearchCV за избор на оптимален брой съседи и начин на претегляне,
# като критерий за оптимизация е Macro F1.
#

# %% cell_id="b76520ff91ac4c268a00c8f032efe6f9" deepnote_block_group="9b24bfe2efa944c8aae21ebc7317c000" deepnote_cell_type="code" deepnote_content_hash="344160ca" deepnote_execution_finished_at="2026-01-27T20:46:02.801Z" deepnote_execution_started_at="2026-01-27T20:39:25.191Z" deepnote_sorting_key="62" deepnote_source="knn_grid = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", KNeighborsClassifier())\n])\n\nparam_grid_knn = {\n    \"model__n_neighbors\": [5, 11, 21],\n    \"model__weights\": [\"uniform\", \"distance\"]\n}\n\ngs_knn = GridSearchCV(\n    estimator=knn_grid,\n    param_grid=param_grid_knn,\n    scoring=\"f1_macro\",\n    cv=3,\n    n_jobs=-1,\n    verbose=1\n)\n\ngs_knn.fit(X_train, y_train)\nprint(\"Best kNN params:\", gs_knn.best_params_)\n\nbest_knn = gs_knn.best_estimator_\n\nbest_knn_results = evaluate_classifier(\n    model_pipeline=best_knn,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=397610 execution_start=1769546365191 id="rx5UsCi_YB7b" outputId="b88db80b-da0b-47c3-b700-62ffa4f58429" source_hash="344160ca"
knn_grid = Pipeline(steps=[
    ("prep", preprocess_cls),
    ("model", KNeighborsClassifier())
])

param_grid_knn = {
    "model__n_neighbors": [5, 11, 21],
    "model__weights": ["uniform", "distance"]
}

gs_knn = GridSearchCV(
    estimator=knn_grid,
    param_grid=param_grid_knn,
    scoring="f1_macro",
    cv=3,
    n_jobs=-1,
    verbose=1
)

gs_knn.fit(X_train, y_train)
print("Best kNN params:", gs_knn.best_params_)

best_knn = gs_knn.best_estimator_

best_knn_results = evaluate_classifier(
    model_pipeline=best_knn,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=False,
    print_report=False
)

# %% [markdown] cell_id="5dc7d76e7e9b4ece9c4fb801dd549bfd" deepnote_block_group="b9fe4444252741109718df9fe4c05d47" deepnote_cell_type="markdown" deepnote_sorting_key="63" deepnote_source="### Support Vector Machine (SVM)\n\n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 \u043b\u0438\u043d\u0435\u0439\u043d\u0430 SVM \u0432\u0435\u0440\u0441\u0438\u044f (`LinearSVC`), \u043a\u043e\u044f\u0442\u043e \u0435 \u043f\u043e-\u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0430 \u0437\u0430 \u0433\u043e\u043b\u0435\u043c\u0438 \u043d\u0430\u0431\u043e\u0440\u0438 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438\n\u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u043d\u0430 CPU. \u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0442\u044a\u0440\u0441\u0438 \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u043d\u0430 \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u0449\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u043b\u043e\u0441\u043a\u043e\u0441\u0442 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n" id="rz9OdgJDYB7b"
# ### Support Vector Machine (SVM)
#
# Използва се линейна SVM версия (`LinearSVC`), която е по-подходяща за големи набори от данни
# и работа на CPU. Моделът търси оптимална разделяща хиперплоскост между жанровете.
#

# %% cell_id="0550b953e8af4d7bb50b86f14fd6ef8f" deepnote_block_group="ba60de93f2144a1288bd803f7905fbfb" deepnote_cell_type="code" deepnote_content_hash="63fb9e22" deepnote_execution_finished_at="2026-01-27T21:09:15.284Z" deepnote_execution_started_at="2026-01-27T20:46:02.861Z" deepnote_sorting_key="64" deepnote_source="svm_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", LinearSVC())\n])\n\nsvm_results = evaluate_classifier(\n    model_pipeline=svm_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1392423 execution_start=1769546762861 id="cQNLyaq-YB7b" outputId="5754a0cd-c00a-4ec9-b1e3-b2a16aa00469" source_hash="63fb9e22"
svm_model = Pipeline(steps=[
    ("prep", preprocess_cls),
    ("model", LinearSVC())
])

svm_results = evaluate_classifier(
    model_pipeline=svm_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=False,
    print_report=False
)

# %% [markdown] cell_id="5b17dedf350342288645f49a45f8c3b7" deepnote_block_group="e53271f9a40a45cdb0d6af89a0970abd" deepnote_cell_type="markdown" deepnote_sorting_key="65" deepnote_source="### Decision Tree \u0438 Random Forest\n\n\u0414\u044a\u0440\u0432\u0435\u0442\u0430\u0442\u0430 \u0437\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u0442 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435.\nRandom Forest \u043a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430 \u0438 \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0434\u0430\u0432\u0430 \u043f\u043e-\u0441\u0442\u0430\u0431\u0438\u043b\u043d\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\n\u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u043e \u0434\u044a\u0440\u0432\u043e.\n" id="yugjlAzBYB7c"
# ### Decision Tree и Random Forest
#
# Дърветата за решения могат да моделират нелинейни зависимости между признаците.
# Random Forest комбинира множество дървета и обикновено дава по-стабилни резултати
# в сравнение с единично дърво.
#

# %% cell_id="9bba37da27d44d4183dbed5cb8a6f11c" deepnote_block_group="0cdec216345240e2b8f4f45d7c27b9bd" deepnote_cell_type="code" deepnote_content_hash="8ae79cdc" deepnote_execution_finished_at="2026-01-27T21:47:58.689Z" deepnote_execution_started_at="2026-01-27T21:47:55.526Z" deepnote_sorting_key="66" deepnote_source="dt_model = Pipeline(steps=[\n    (\"prep\", \"passthrough\"),\n    (\"model\", DecisionTreeClassifier(\n        random_state=42,\n        max_depth=20,\n        min_samples_leaf=5\n    ))\n])\n\ndt_results = evaluate_classifier(\n    model_pipeline=dt_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=3163 execution_start=1769550475526 id="A3dfBc9LYB7c" outputId="6af16999-a100-4b52-afd7-63d80d7a205f" source_hash="8ae79cdc"
dt_model = Pipeline(steps=[
    ("prep", "passthrough"),
    ("model", DecisionTreeClassifier(
        random_state=42,
        max_depth=20,
        min_samples_leaf=5
    ))
])

dt_results = evaluate_classifier(
    model_pipeline=dt_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=False,
    print_report=False
)

# %% cell_id="b0f468d48afc4d3e99e90810e8c0108e" deepnote_block_group="65013a9a68dc48b0927473786352a126" deepnote_cell_type="code" deepnote_content_hash="f6df638e" deepnote_execution_finished_at="2026-01-27T21:48:38.014Z" deepnote_execution_started_at="2026-01-27T21:48:04.280Z" deepnote_sorting_key="67" deepnote_source="rf_model = Pipeline(steps=[\n    (\"prep\", \"passthrough\"),\n    (\"model\", RandomForestClassifier(\n        n_estimators=80,\n        max_depth=20,\n        min_samples_leaf=3,\n        random_state=42,\n        n_jobs=1\n    ))\n])\n\nrf_results = evaluate_classifier(\n    model_pipeline=rf_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=True,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=33734 execution_start=1769550484280 id="BTp6_oejYB7c" outputId="93e21e9c-9b2e-4f2f-aae5-fda8add49943" source_hash="f6df638e"
rf_model = Pipeline(steps=[
    ("prep", "passthrough"),
    ("model", RandomForestClassifier(
        n_estimators=80,
        max_depth=20,
        min_samples_leaf=3,
        random_state=42,
        n_jobs=1
    ))
])

rf_results = evaluate_classifier(
    model_pipeline=rf_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=True,
    print_report=False
)

# %% [markdown] id="S0uHkGyUkjBk"
# ### XGBoost (XGBClassifier)

# %% id="4rq7880lkwuE"
# !pip -q install xgboost

# %% id="YU7yRYXrkzFT"
from xgboost import XGBClassifier
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


# %% colab={"base_uri": "https://localhost:8080/", "height": 556} id="4SA3m8LfksxP" outputId="a93a9444-833f-4b63-f042-acde4e031bf8"
class XGBGenreClassifier(BaseEstimator, ClassifierMixin):
    def __init__(
        self,
        n_estimators=300,
        max_depth=8,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_lambda=1.0,
        random_state=42,
        n_jobs=-1
    ):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.learning_rate = learning_rate
        self.subsample = subsample
        self.colsample_bytree = colsample_bytree
        self.reg_lambda = reg_lambda
        self.random_state = random_state
        self.n_jobs = n_jobs

    def fit(self, X, y):
        self.le_ = LabelEncoder()
        y_enc = self.le_.fit_transform(y)

        self.model_ = XGBClassifier(
            n_estimators=self.n_estimators,
            max_depth=self.max_depth,
            learning_rate=self.learning_rate,
            subsample=self.subsample,
            colsample_bytree=self.colsample_bytree,
            reg_lambda=self.reg_lambda,
            objective="multi:softprob",
            eval_metric="mlogloss",
            tree_method="hist",
            random_state=self.random_state,
            n_jobs=self.n_jobs,
            num_class=len(self.le_.classes_)
        )
        self.model_.fit(X, y_enc)
        return self

    def predict(self, X):
        pred_enc = self.model_.predict(X)
        return self.le_.inverse_transform(pred_enc)


# %%
# Pipeline като при RandomForest (без scaling)
xgb_model = Pipeline(steps=[
    ("prep", "passthrough"),
    ("model", XGBGenreClassifier(
        n_estimators=300,
        max_depth=8,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1
    ))
])

xgb_results = evaluate_classifier(
    model_pipeline=xgb_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=True,
    print_report=False
)

xgb_results


# %% [markdown] cell_id="ba6f4cba130344959ea3f714d456c850" deepnote_block_group="5b29c57ea3a64cb98ba7376553b8eb10" deepnote_cell_type="markdown" deepnote_sorting_key="68" deepnote_source="### MLPClassifier\n\nMLPClassifier \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0432\u0430 \u043c\u043d\u043e\u0433\u043e\u0441\u043b\u043e\u0435\u043d \u043f\u0435\u0440\u0446\u0435\u043f\u0442\u0440\u043e\u043d, \u043a\u043e\u0439\u0442\u043e \u043c\u043e\u0436\u0435 \u0434\u0430 \u0443\u043b\u0430\u0432\u044f \u0441\u043b\u043e\u0436\u043d\u0438 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0441\u043b\u0443\u0436\u0438 \u043a\u0430\u0442\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043f\u043e\u0434\u0445\u043e\u0434 \u043e\u0442 \u0443\u0447\u0435\u0431\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b.\n" id="k0trGmWZYB7c"
# ### MLPClassifier
#
# MLPClassifier представлява многослоен перцептрон, който може да улавя сложни нелинейни зависимости.
# Моделът служи като допълнителен сравнителен подход от учебния материал.
#

# %% cell_id="7299629268de410692c2f0c504927502" deepnote_block_group="7c5b5878829644428b468b9f2d30cb91" deepnote_cell_type="code" deepnote_content_hash="5c560f01" deepnote_execution_finished_at="2026-01-27T21:59:48.094Z" deepnote_execution_started_at="2026-01-27T21:48:38.071Z" deepnote_sorting_key="69" deepnote_source="mlp_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", MLPClassifier(\n        hidden_layer_sizes=(64, 32),\n        activation=\"relu\",\n        solver=\"adam\",\n        max_iter=60,\n        batch_size=512,\n        early_stopping=True,\n        validation_fraction=0.1,\n        n_iter_no_change=8,\n        random_state=42\n    ))\n])\n\nmlp_results = evaluate_classifier(\n    model_pipeline=mlp_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=670023 execution_start=1769550518071 id="xraYb__VYB7c" outputId="1e8cf473-f58e-47d5-c91d-79b1a8032f07" source_hash="5c560f01"
mlp_model = Pipeline(steps=[
    ("prep", preprocess_cls),
    ("model", MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation="relu",
        solver="adam",
        max_iter=60,
        batch_size=512,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=8,
        random_state=42
    ))
])

mlp_results = evaluate_classifier(
    model_pipeline=mlp_model,
    X_train=X_train, y_train=y_train,
    X_test=X_test, y_test=y_test,
    top_n=10,
    show_confusion=False,
    print_report=False
)

# %% [markdown] cell_id="dea4ec7c106c415fa60dd2ecb59649d8" deepnote_block_group="d548225f8cd240858064b96413bb0c29" deepnote_cell_type="markdown" deepnote_sorting_key="70" deepnote_source="## \u0418\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440)\n\n### \u041e\u0431\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435\u0442\u043e\n\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u0435 \u0442\u0440\u0443\u0434\u043d\u0430 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u043d\u0430 \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435, \u043d\u043e \u0432\u0441\u0435 \u043f\u0430\u043a \u0438\u043c\u0430 \u044f\u0441\u043d\u0438 \u0440\u0430\u0437\u043b\u0438\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435:\n\n- **Logistic Regression**: Accuracy = 0.1984, Macro F1 = 0.1694  \n  \u041b\u0438\u043d\u0435\u0435\u043d \u0431\u0430\u0437\u043e\u0432 \u043c\u043e\u0434\u0435\u043b. \u0414\u0430\u0432\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u043d\u043e \u043d\u0438\u0441\u043a\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043d\u0435 \u0441\u0430 \u0434\u043e\u0431\u0440\u0435 \u043b\u0438\u043d\u0435\u0439\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u0438 \u0441\u0430\u043c\u043e \u043f\u043e \u0442\u0435\u0437\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438.\n\n- **kNN**: Accuracy = 0.2137, Macro F1 = 0.2042  \n  \u041f\u043e\u0434\u043e\u0431\u0440\u044f\u0432\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0441\u043f\u0440\u044f\u043c\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u0438\u044f baseline, \u043a\u043e\u0435\u0442\u043e \u0435 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e, \u0437\u0430\u0449\u043e\u0442\u043e \u043c\u0435\u0442\u043e\u0434\u044a\u0442 \u0443\u043b\u0430\u0432\u044f \u043b\u043e\u043a\u0430\u043b\u043d\u0438 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\n- **kNN + GridSearch**: Accuracy = 0.2207, Macro F1 = 0.2158  \n  \u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 (k=21, weights=distance) \u0432\u043e\u0434\u0438 \u0434\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e (\u0443\u043c\u0435\u0440\u0435\u043d\u043e) \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0435 \u2014 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0442\u0430 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u0438\u043c\u0430 \u0440\u0435\u0430\u043b\u0435\u043d \u0435\u0444\u0435\u043a\u0442.\n\n- **SVM (LinearSVC)**: Accuracy = 0.1723, Macro F1 = 0.1111  \n  \u041d\u0430\u0439-\u0441\u043b\u0430\u0431\u0438\u044f\u0442 \u043c\u043e\u0434\u0435\u043b \u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u043e\u0441\u0442\u0430\u043d\u0430\u043b\u0438\u0442\u0435. ConvergenceWarning \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0438\u0433\u043d\u0430\u043b\u0430 \u0441\u0442\u0430\u0431\u0438\u043b\u043d\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u0437\u0430\u0434\u0430\u0434\u0435\u043d\u0438\u0442\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0438, \u0430 \u043e\u0441\u0432\u0435\u043d \u0442\u043e\u0432\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u0430\u0442\u0430 \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u0430 \u0437\u0430 \u0434\u043e\u0431\u0440\u0435 \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n\n- **Decision Tree**: Accuracy = 0.2302, Macro F1 = 0.2314  \n  \u041f\u043e-\u0434\u043e\u0431\u0440\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435 \u043e\u0442 \u043b\u0438\u043d\u0435\u0439\u043d\u0438\u0442\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u0438. \u0414\u044a\u0440\u0432\u043e\u0442\u043e \u043c\u043e\u0436\u0435 \u0434\u0430 \u0443\u043b\u0430\u0432\u044f \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u043a\u0430\u0442\u043e \u0435\u0434\u0438\u043d\u0438\u0447\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u0435 \u043f\u043e-\u043d\u0435\u0441\u0442\u0430\u0431\u0438\u043b\u043d\u043e \u0438 \u043b\u0435\u0441\u043d\u043e \u043d\u0430\u0443\u0447\u0430\u0432\u0430 \u0448\u0443\u043c/\u0441\u043f\u0435\u0446\u0438\u0444\u0438\u0447\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\n- **Random Forest**: Accuracy = 0.3205, Macro F1 = 0.3112  \n  \u041d\u0430\u0439-\u0434\u043e\u0431\u0440\u0438\u044f\u0442 \u043c\u043e\u0434\u0435\u043b. \u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f\u0442\u0430 \u043e\u0442 \u043c\u043d\u043e\u0433\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430 \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f\u0442\u0430 \u0438 \u0443\u043b\u0430\u0432\u044f \u043f\u043e-\u0441\u043b\u043e\u0436\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435, \u043a\u043e\u0435\u0442\u043e \u0432\u043e\u0434\u0438 \u0434\u043e \u043e\u0441\u0435\u0437\u0430\u0435\u043c\u043e \u043f\u043e-\u0434\u043e\u0431\u0440\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438.\n\n- **MLPClassifier**: Accuracy = 0.2865, Macro F1 = 0.2651  \n  \u0421\u0438\u043b\u0435\u043d \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442, \u043d\u043e \u043f\u043e\u0434 Random Forest. ConvergenceWarning \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043f\u0440\u0438 \u043f\u043e\u0432\u0435\u0447\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0438 (\u0438\u043b\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438) \u0435 \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0435, \u043d\u043e \u0442\u043e\u0432\u0430 \u0442\u0440\u044f\u0431\u0432\u0430 \u0434\u0430 \u0441\u0435 \u0431\u0430\u043b\u0430\u043d\u0441\u0438\u0440\u0430 \u0441\u043f\u0440\u044f\u043c\u043e \u0432\u0440\u0435\u043c\u0435\u0442\u043e/\u0440\u0435\u0441\u0443\u0440\u0441\u0438\u0442\u0435 \u0432 \u0441\u0440\u0435\u0434\u0430\u0442\u0430.\n\n**\u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0430 \u0431\u0435\u043b\u0435\u0436\u043a\u0430:** Confusion matrix \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u043f\u043e\u0447\u0442\u0438 \u043f\u0440\u0430\u0437\u043d\u0430 (\u0447\u0435\u0440\u043d\u0430 \u0438\u0437\u0432\u044a\u043d \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0430). \u041f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f (\u0432 \u0441\u043b\u0443\u0447\u0430\u044f \u0438\u043c\u0430\u043c\u0435 \u043c\u043d\u043e\u0433\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435) \u0433\u0440\u0435\u0448\u043a\u0438\u0442\u0435 \u0441\u0435 \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0442 \u043c\u0435\u0436\u0434\u0443 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0434\u0440\u0443\u0433\u0438 \u043a\u043b\u0430\u0441\u043e\u0432\u0435 \u0438 \u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u043a\u043b\u0435\u0442\u043a\u0438 \u0438\u0437\u0432\u044a\u043d \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0430 \u0438\u043c\u0430\u0442 \u043c\u043d\u043e\u0433\u043e \u043c\u0430\u043b\u043a\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0447\u0435\u0441\u0442\u043e 0\u20132). \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043c\u0435 Top-N (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 10) \u0436\u0430\u043d\u0440\u0430, \u043a\u043e\u0435\u0442\u043e \u043f\u0440\u0430\u0432\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u0430\u0442\u0430 \u0447\u0435\u0442\u0438\u043c\u0430, \u043d\u043e \u0433\u0440\u0435\u0448\u043a\u0438\u0442\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u043e\u0442 \u0442\u0435\u0437\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0447\u0435\u0441\u0442\u043e \u0441\u0430 \u043a\u044a\u043c \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438\u0437\u0432\u044a\u043d Top-N. \u0412 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0437\u0430 \u0432\u0441\u0438\u0447\u043a\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u0430\u0442\u0430 \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0441\u0445\u043e\u0434\u043d\u043e: \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044a\u0442 \u0435 \u043d\u0430\u0439-\u0441\u0432\u0435\u0442\u044a\u043b, \u0430 \u0438\u0437\u0432\u044a\u043d \u043d\u0435\u0433\u043e \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\u0442\u0435 \u0441\u0430 \u0440\u0430\u0437\u043f\u0440\u044a\u0441\u043d\u0430\u0442\u0438 \u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u043e \u043f\u043e\u0447\u0442\u0438 \u043d\u0435 \u0441\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u0432\u0430\u0442.\n\n### \u0417\u0430\u0449\u043e \u043d\u044f\u043a\u043e\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043f\u043e-\u0434\u043e\u0431\u0440\u0435 \u043e\u0442 \u0434\u0440\u0443\u0433\u0438\n\n\u0420\u0430\u0437\u043b\u0438\u043a\u0438\u0442\u0435 \u0432 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0438\u0434\u0432\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u043d\u043e \u043e\u0442 \u0442\u043e\u0432\u0430 \u043a\u0430\u043a \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u043e\u043f\u0438\u0441\u0432\u0430\u0442 \u0432\u0440\u044a\u0437\u043a\u0430\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438 \u0436\u0430\u043d\u0440\u0430. \u041b\u0438\u043d\u0435\u0439\u043d\u0438\u044f\u0442 baseline (Logistic Regression) \u0438\u043c\u0430 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0434\u0430 \u043d\u0430\u043c\u0438\u0440\u0430 \u0441\u0430\u043c\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0433\u0440\u0430\u043d\u0438\u0446\u0438 \u043c\u0435\u0436\u0434\u0443 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435, \u0430 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0431\u043b\u0438\u0437\u043a\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u0438 \u0442\u043e\u0432\u0430 \u0447\u0435\u0441\u0442\u043e \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u043e. kNN \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f \u043f\u043e-\u0434\u043e\u0431\u0440\u0435, \u0437\u0430\u0449\u043e\u0442\u043e \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043b\u043e\u043a\u0430\u043b\u043d\u043e \u0441\u0445\u043e\u0434\u0441\u0442\u0432\u043e \u0438 \u0443\u043b\u0430\u0432\u044f \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u0435 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a\u044a\u043c \u0448\u0443\u043c \u0438 \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0435 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435. Decision Tree \u043c\u043e\u0436\u0435 \u0434\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0441\u0442\u0438, \u043d\u043e \u043a\u0430\u0442\u043e \u0435\u0434\u0438\u043d\u0438\u0447\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u0435 \u043d\u0435\u0441\u0442\u0430\u0431\u0438\u043b\u0435\u043d \u0438 \u0441\u043a\u043b\u043e\u043d\u0435\u043d \u043a\u044a\u043c overfitting. Random Forest \u0434\u0430\u0432\u0430 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u0437\u0430\u0449\u043e\u0442\u043e \u0443\u0441\u0440\u0435\u0434\u043d\u044f\u0432\u0430 \u043c\u043d\u043e\u0433\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430, \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f\u0442\u0430 \u0438 \u0443\u043b\u0430\u0432\u044f \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 (\u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438), \u043a\u043e\u0435\u0442\u043e \u0435 \u0432\u0430\u0436\u043d\u043e \u0437\u0430 \u0441\u043b\u043e\u0436\u043d\u0430 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043a\u0430\u0442\u043e \u0442\u0430\u0437\u0438. MLP \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0432\u0438\u0441\u043e\u043a\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0441\u044a\u0449\u043e \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435\u0442\u043e \u043c\u0443 \u0435 \u043f\u043e-\u0442\u0440\u0443\u0434\u043d\u043e \u0437\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u043c\u043e\u0436\u0435 \u0434\u0430 \u043d\u0435 \u043a\u043e\u043d\u0432\u0435\u0440\u0433\u0438\u0440\u0430 \u043d\u0430\u043f\u044a\u043b\u043d\u043e \u043f\u0440\u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u0438.\n\n### \u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0438 \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u0438 \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f\n\n\u041d\u0430\u0439-\u0434\u043e\u0431\u044a\u0440 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0432 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430 Random Forest, \u043d\u043e \u0434\u043e\u0440\u0438 \u0442\u043e\u0439 \u043d\u0435 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u043c\u043d\u043e\u0433\u043e \u0432\u0438\u0441\u043e\u043a\u0430 \u0442\u043e\u0447\u043d\u043e\u0441\u0442, \u043a\u043e\u0435\u0442\u043e \u0435 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e \u043f\u0440\u0438 \u0433\u043e\u043b\u044f\u043c \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u0449\u0438 \u0441\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438. \u0421\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u043d\u043e \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u043e \u0434\u043e\u0431\u044a\u0440 \u0437\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u043e\u0434\u0445\u043e\u0434\u0430 \u0438 \u0437\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437 \u043c\u0435\u0436\u0434\u0443 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438, \u043d\u043e \u043d\u0435 \u0435 \u201c\u043f\u0435\u0440\u0444\u0435\u043a\u0442\u043d\u043e\u201d \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0437\u0430 \u043d\u0430\u0434\u0435\u0436\u0434\u043d\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u043e \u0440\u0430\u0437\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0435. \u041f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u0438 \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f \u0441\u0430: \u043f\u043e-\u0437\u0430\u0434\u044a\u043b\u0431\u043e\u0447\u0435\u043d\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 (\u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043e \u0441\u043f\u0440\u044f\u043c\u043e \u0440\u0435\u0441\u0443\u0440\u0441\u0438\u0442\u0435), \u0434\u043e\u0431\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043d\u0430\u043f\u0440. \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u0434\u0430\u043d\u043d\u0438 \u0438\u043b\u0438 \u043f\u043e-\u0431\u043e\u0433\u0430\u0442\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0438\u044f), \u043e\u0431\u0435\u0434\u0438\u043d\u044f\u0432\u0430\u043d\u0435/\u0439\u0435\u0440\u0430\u0440\u0445\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u0441\u0445\u043e\u0434\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (\u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430\u043d\u0435 \u043d\u0430 \u0431\u0440\u043e\u044f \u043a\u043b\u0430\u0441\u043e\u0432\u0435), \u0438 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u043e-\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u0437\u0430 \u0430\u0443\u0434\u0438\u043e (\u043d\u0430\u043f\u0440. \u043c\u043e\u0434\u0435\u043b\u0438 \u0432\u044a\u0440\u0445\u0443 \u0441\u043f\u0435\u043a\u0442\u0440\u043e\u0433\u0440\u0430\u043c\u0438 \u0438\u043b\u0438 embedding-\u0438).\n\n\n### \u0418\u0437\u0432\u043e\u0434 \u043e\u0442 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f\u0442\u0430\n\u041d\u0430\u0439-\u0434\u043e\u0431\u044a\u0440 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0434\u0430\u0432\u0430 **Random Forest**, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0437\u0430 \u0442\u0435\u0437\u0438 \u0434\u0430\u043d\u043d\u0438 \u0441\u0430 \u0432\u0430\u0436\u043d\u0438 **\u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0438 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435**. \u0421\u043b\u0435\u0434\u0432\u0430\u0449\u0438\u044f\u0442 \u043b\u043e\u0433\u0438\u0447\u0435\u043d \u0438\u0437\u0431\u043e\u0440 \u0435 \u0442\u043e\u0437\u0438 \u043c\u043e\u0434\u0435\u043b \u0434\u0430 \u0431\u044a\u0434\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d \u043a\u0430\u0442\u043e \u043e\u0441\u043d\u043e\u0432\u0435\u043d \u0437\u0430 \u0444\u0438\u043d\u0430\u043b\u043d\u0430\u0442\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435.\n" id="HHFiaAgsYB7c"
# ## Интерпретация на резултатите (класификация на жанр)
#
# ### Обобщение на представянето
# Сравнените модели показват, че задачата е трудна при много на брой жанрове, но все пак има ясни разлики между алгоритмите:
#
# - **Logistic Regression**: Accuracy = 0.1984, Macro F1 = 0.1694  
#   Линеен базов модел. Дава сравнително ниски резултати, което подсказва, че жанровете не са добре линейно разделими само по тези признаци.
#
# - **kNN**: Accuracy = 0.2137, Macro F1 = 0.2042  
#   Подобрява резултатите спрямо линейния baseline, което е очаквано, защото методът улавя локални нелинейни зависимости.
#
# - **kNN + GridSearch**: Accuracy = 0.2207, Macro F1 = 0.2158  
#   Оптимизацията (k=21, weights=distance) води до допълнително (умерено) подобрение — показва, че настройката на параметрите има реален ефект.
#
# - **SVM (LinearSVC)**: Accuracy = 0.1723, Macro F1 = 0.1111  
#   Най-слабият модел в сравнение с останалите. ConvergenceWarning подсказва, че оптимизацията не е достигнала стабилно решение при зададените итерации, а освен това линейната граница вероятно не е достатъчна за добре разделяне на жанровете.
#
# - **Decision Tree**: Accuracy = 0.2302, Macro F1 = 0.2314  
#   По-добро представяне от линейните подходи. Дървото може да улавя нелинейни зависимости, но като единичен модел е по-нестабилно и лесно научава шум/специфични зависимости.
#
# - **Random Forest**: Accuracy = 0.3205, Macro F1 = 0.3112  
#   Най-добрият модел. Комбинацията от много дървета намалява дисперсията и улавя по-сложни зависимости между признаците, което води до осезаемо по-добри резултати.
#
# * **XGBoost (XGBClassifier)**: Accuracy = 0.2976, Macro F1 = 0.2890
#   Допълнителен силен модел на базата на градиентно буустинг дървета, но в нашия случай **не надмина Random Forest**. Вероятна причина е **високият брой класове (жанрове)** и припокриването между тях, при което ансамбълът от случайни дървета се оказва по-стабилен спрямо шум и дисбаланс.
#
# - **MLPClassifier**: Accuracy = 0.2865, Macro F1 = 0.2651  
#   Силен резултат, но под Random Forest. ConvergenceWarning показва, че при повече итерации (или различни настройки) е възможно допълнително подобрение, но това трябва да се балансира спрямо времето/ресурсите в средата.
#
# **Допълнителна бележка:** Confusion matrix изглежда почти празна (черна извън диагонала). При многокласова класификация (в случая имаме много жанрове) грешките се разпределят между множество други класове и повечето клетки извън диагонала имат много малки стойности (често 0–2). Визуализираме Top-N (например 10) жанра, което прави матрицата четима, но грешките на песните от тези жанрове често са към жанрове извън Top-N. В резултат за всички модели матрицата изглежда сходно: диагоналът е най-светъл, а извън него стойностите са разпръснати и визуално почти не се отличават.
#
# ### Защо някои алгоритми се справят по-добре от други
#
# Разликите в резултатите идват основно от това как моделите могат да описват връзката между признаците и жанра. Линейният baseline (Logistic Regression) има ограничение да намира само линейни граници между класовете, а при много жанрове и близки аудио профили това често не е достатъчно. kNN се представя по-добре, защото използва локално сходство и улавя нелинейни зависимости, но е чувствителен към шум и припокриване между жанрове. Decision Tree може да моделира нелинейности, но като единичен модел е нестабилен и склонен към overfitting. Random Forest дава най-добри резултати, защото усреднява много дървета, намалява дисперсията и улавя взаимодействия между признаците (нелинейни комбинации), което е важно за сложна многокласова задача като тази. MLP постига високи резултати, тъй като също моделира нелинейни зависимости, но обучението му е по-трудно за настройка и може да не конвергира напълно при ограничени ресурси.
#
# ### Заключение и възможни подобрения
#
# Най-добър резултат в експериментите показва Random Forest, но дори той не постига много висока точност, което е очаквано при голям брой жанрове и частично припокриващи се аудио характеристики. Следователно моделът е достатъчно добър за демонстрация на подхода и за сравнителен анализ между алгоритми, но не е “перфектно” решение за надеждно жанрово разпознаване. Потенциални подобрения са: по-задълбочена настройка на хиперпараметри (ограничено спрямо ресурсите), добавяне на допълнителни характеристики (напр. текстови данни или по-богати аудио представяния), обединяване/йерархизация на сходни жанрове (намаляване на броя класове), и използване на по-специализирани модели за аудио (напр. модели върху спектрограми или embedding-и).
#
#
# ### Извод от сравненията
# Най-добър резултат дава **Random Forest**, което показва, че за тези данни са важни **нелинейни зависимости и взаимодействия между признаците**. Следващият логичен избор е този модел да бъде използван като основен за финалната оценка и ограничена оптимизация на параметрите.
#

# %% [markdown] id="PaNUawkeYB7d"
# # Част 2. Кластъризация

# %% [markdown] id="ezQy9F0KYB7d"
# ## Подготовка на данни за клъстеризация
#
# При клъстеризация целта е да се групират песни без предварително зададени етикети (unsupervised learning). Вместо да предсказваме жанр, търсим естествени групи в данните, базирани на сходство в аудио характеристиките.
#
# **Основни разлики спрямо класификацията:**
# - Няма целева променлива (`track_genre`)
# - Фокус върху аудио характеристики, свързани със звучене и настроение
# - Scaling е критичен, тъй като алгоритмите са distance-based (напр. K-Means, DBSCAN)
# - Не се прави train/test split (всички данни се използват за клъстеризация)

# %% colab={"base_uri": "https://localhost:8080/"} id="uPkShIcaYB7d" outputId="1bf3bee0-eaa3-4ba6-ffa3-0f8d026179a2"
# Подготовка на данни за клъстеризация
df_clust = df.copy()

# Премахване на дубликати и редове с липсващи стойности
df_clust = df_clust.drop_duplicates()
df_clust = df_clust.dropna()

# Explicit към числова стойност
if "explicit" in df_clust.columns:
    df_clust["explicit"] = df_clust["explicit"].astype(int)

print(f"Размер на данните за клъстеризация: {df_clust.shape}")

# %% colab={"base_uri": "https://localhost:8080/", "height": 241} id="Ibo_NzeNYB7d" outputId="dce724c1-15a2-4400-958d-45e7d4526762"
# Избор на аудио признаци за клъстеризация
# Фокусираме се върху характеристики, описващи звучене и настроение
audio_features = [
    "danceability",     # Танцувалност (0-1)
    "energy",           # Енергичност (0-1)
    "loudness",         # Сила на звука (обикновено -60 до 0 dB)
    "speechiness",      # Присъствие на говор (0-1)
    "acousticness",     # Акустичност (0-1)
    "instrumentalness", # Инструментална (0-1)
    "liveness",         # "Живост" / присъствие на публика (0-1)
    "valence",          # Позитивност/настроение (0-1)
    "tempo"             # Темпо (BPM)
]

# Махаме track_genre (нямаме target variable при unsupervised learning)
# Махаме text columns и ID-та
X_clust = df_clust[audio_features].copy()

print(f"Избрани признаци за клъстеризация: {audio_features}")
print(f"Размер на матрицата: {X_clust.shape}")
X_clust.head()

# %% colab={"base_uri": "https://localhost:8080/", "height": 224} id="HHP51QsbYB7d" outputId="f648aefe-d0ed-4ac1-ac2d-cdf232efb37a"
# Нормализация (Scaling) за клъстеризация
# Използваме StandardScaler, защото признаците имат различни мащаби
# (напр. loudness е в dB, tempo е BPM, а останалите са 0-1)
scaler_clust = StandardScaler()
X_clust_scaled = scaler_clust.fit_transform(X_clust)

# Преобразуваме обратно в DataFrame за по-лесна работа
X_clust_scaled_df = pd.DataFrame(
    X_clust_scaled,
    columns=audio_features,
    index=X_clust.index
)

print(f"Размер на нормализираните данни: {X_clust_scaled_df.shape}")
X_clust_scaled_df.head()

# %% id="jilw52w6YB7d" outputId="28a43c2f-74f3-4190-8a73-45fff6ad347e"
print("Статистики след нормализация:")
print(X_clust_scaled_df.describe())

# %% [markdown] id="VA8df9s3YB7d"
# ### Optional: Намаляване на размерност с PCA
#
# За улеснение на визуализацията и евентуално ускоряване на алгоритмите можем да приложим PCA (Principal Component Analysis). Това намалява броя на признаците, като запазва най-важната информация.

# %% id="aPKB8uLMYB7e" outputId="fa0bd2f9-4861-467c-b668-1ba6d681119e"
# Прилагане на PCA (запазваме напр. 95% от вариацията)
pca = PCA(n_components=0.95, random_state=42)
X_clust_pca = pca.fit_transform(X_clust_scaled)

print(f"Оригинален брой признаци: {X_clust_scaled.shape[1]}")
print(f"Брой компоненти след PCA (95% variance): {pca.n_components_}")
print(f"Обяснена вариация по компоненти: {pca.explained_variance_ratio_}")
print(f"Обща обяснена вариация: {pca.explained_variance_ratio_.sum():.4f}")

# %% id="z4X-02mkYB7e" outputId="eccaeae3-7393-4eb7-8a95-0f5718f26b54"
X_clust_scaled_df.columns

# %% id="jcZTOGXDYB7e" outputId="909793c3-973c-4255-899a-6748aec4844f"
# Визуализация на обяснената вариация по компоненти
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(range(1, pca.n_components_ + 1), pca.explained_variance_ratio_)
plt.xlabel("Principal Component")
plt.ylabel("Explained Variance Ratio")
plt.title("Explained Variance by Component")

plt.subplot(1, 2, 2)
plt.plot(range(1, pca.n_components_ + 1),
         np.cumsum(pca.explained_variance_ratio_), marker='o')
plt.xlabel("Number of Components")
plt.ylabel("Cumulative Explained Variance")
plt.title("Cumulative Explained Variance")
plt.axhline(y=0.95, color='r', linestyle='--', label='95% threshold')
plt.legend()

plt.tight_layout()
plt.show()

# %% [markdown] id="VFwIaacjYB7e"
# От тази визуализация можем да разберем, че данните са комплексни и всички признаци са важни – дори най-слабо обяснителният компонент допринася около 5% от общата вариация. Това показва, че за постигане на 95% запазена вариация са необходими повечето от първоначалните характеристики, което подчертава сложността на музикалните данни.

# %% [markdown] id="uumdhsVXYB7e"
# ## Разделяне на клъстъри

# %% id="yH7KNDsBYB7e"
from scipy.cluster.hierarchy import dendrogram, linkage

# %% colab={"base_uri": "https://localhost:8080/"} id="U7IAEp1qYB7f" outputId="abdda3c8-75b2-4f3f-9c31-0f11b0bd9c81"
# Hierarchical clustering изисква много памет за пълния dataset
# Използваме стратифициран sample с еднакъв брой песни от всеки жанр
songs_per_genre = 350  # Еднакъв брой песни от всеки жанр
# songs_per_genre = 50  # TODO: да се смени на колкото трябва, аз използвам само 50, защото иначе RAM-ът ми свършва
np.random.seed(42)

# Стратифициран sampling
sample_indices = []
for genre in df_clust['track_genre'].unique():
    genre_indices = df_clust[df_clust['track_genre'] == genre].index
    sampled = np.random.choice(genre_indices, size=min(songs_per_genre, len(genre_indices)), replace=False)
    sample_indices.extend(sampled)

X_sample = X_clust_scaled[df_clust.index.isin(sample_indices)]

total_genres = df_clust['track_genre'].nunique()
print(f"Използван стратифициран sample: {songs_per_genre} песни × {total_genres} жанра = {len(sample_indices)} песни")

# %% id="tqyRPlJojCug"
linked = linkage(X_sample, method='ward')

# %% id="orBoc-VjYB7f"
linked_complete = linkage(X_sample, method='complete')

# %% id="witYWuwwYB7f"
linked_average = linkage(X_sample, method='average')

# %% id="IOQ9qbvrYB7f" outputId="f93364cd-924b-430a-9bcf-9d57b8892aea"
fig, axes = plt.subplots(1, 3, figsize=(18, 7))

dendrogram(linked, truncate_mode='level', p=6, ax=axes[0])
axes[0].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Ward Linkage)")
axes[0].axhline(y=96, color='r', linestyle='-')

dendrogram(linked_complete, truncate_mode='level', p=6, ax=axes[1])
axes[1].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Complete Linkage)")
# axes[1].axhline(y=10.5, color='r', linestyle='-')

dendrogram(linked_average, truncate_mode='level', p=6, ax=axes[2])
axes[2].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Average Linkage)")
# axes[2].axhline(y=6.2, color='r', linestyle='-')

plt.tight_layout()
plt.show()

# %% id="l7djA6OOYB7f" outputId="9eb6dafc-3585-44a5-b856-45a946de2128"
import matplotlib.pyplot as plt
import numpy as np

last_number_of_distances = 70
# Взимаме последните 20 дистанции за всеки linkage метод
last = linked[-last_number_of_distances:, 2]
last_rev = last[::-1]

last_complete = linked_complete[-last_number_of_distances:, 2]
last_rev_complete = last_complete[::-1]

last_average = linked_average[-last_number_of_distances:, 2]
last_rev_average = last_average[::-1]

idxs = np.arange(1, len(last) + 1)

fig, axes = plt.subplots(1, 3, figsize=(18, 7))

axes[0].plot(idxs, last_rev, label='Ward Distances')
axes[0].set_title('Elbow Method за избор на k')
axes[0].set_xlabel('Брой клъстери (k)')
axes[0].set_ylabel('Разстояние (Ward linkage cost)')
axes[0].grid(True)

axes[1].plot(idxs, last_rev_complete, label='Complete Distances')
axes[1].set_title('Elbow Method за избор на k')
axes[1].set_xlabel('Брой клъстери (k)')
axes[1].set_ylabel('Разстояние (Complete linkage cost)')
axes[1].grid(True)

axes[2].plot(idxs, last_rev_average, label='Average Distances')
axes[2].set_title('Elbow Method за избор на k')
axes[2].set_xlabel('Брой клъстери (k)')
axes[2].set_ylabel('Разстояние (Average linkage cost)')
axes[2].grid(True)

plt.show()

# %% [markdown] id="jsfh2YjcYB7f"
# ### Анализ на дендрограмите и избор на k
#
# С помощта на функцията `linkage` от scipy и метода на Ward генерирахме йерархия на клъстерите. За да определим оптималния брой клъстери (k), анализирахме дендрограмите, търсейки най-голямото вертикално разстояние (gap) между последователни обединявания. Голямата дължина на вертикалните линии при метода на Ward индикира значително нарастване на вътрешната вариация при обединяване, което математически подсказва, че клъстерите преди сливането са добре разграничени.
#
# На графиките се вижда, че k=2 или k=3 са математически най-обособените разделения. В нашия случай обаче те не са подходящи, тъй като целта е данните да се разделят на достатъчен брой клъстери, за да се постигне смислено групиране по настроение/звучене.
#
# Според резултатите от Elbow Method, приложен върху дистанциите при Ward Linkage, се наблюдава, че след определена стойност на k намалението на общата вътрешноклъстерна дистанция (cost) става значително по-слабо. Elbow Method идентифицира тази „точка на пречупване“, при която добавянето на повече клъстери вече не води до съществено подобрение на качеството на клъстеризацията.
#
# В анализа си основно се опираме на Ward Linkage, тъй като този метод минимизира вътрешноклъстерната дисперсия и е най-подходящ за нашите цели — формиране на възможно най-плътни (dense) и компактни клъстери.
#
# Според дендограмата и Elbow Method, k = 10 е много добър избор. Въпреки това ще потвърдим този резултат чрез Grid Search, за да бъдем напълно сигурни в избора си.

# %% [markdown] id="RNEqH4aCYB7f"
# ### Grid Search за оптимално k
#
# За да изберем най-добрия брой клъстери, ще изпълним grid search с различни метрики за оценка:
# - **Silhouette Score** - мери колко добре всеки обект пасва на своя клъстър (стойности от -1 до 1, по-високи са по-добри)
# - **Calinski-Harabasz Score** - съотношение на между-клъстерна и вътрешно-клъстерна дисперсия (по-високо е по-добре)
# - **Davies-Bouldin Score** - средна прилика между клъстери (по-ниско е по-добре)

# %% [markdown] id="iWJm44T0YB7g"
# Заради проблема с изискването на голям обем RAM (и цената за RAM), трябва да измислим оптимизация. Планирам да направя клъстеринг само върху представителна извадка (sample) от данните. След това ще използвам KNN (K-Nearest Neighbors), за да класифицирам останалите данни към вече създадените клъстери. По този начин процесът на клъстериране ще се оптимизира значително

# %% id="aA0DxPEcYB7g"
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.cluster import AgglomerativeClustering

# %% id="_eESq3pAYB7g" outputId="826f2031-a0b4-4e80-d80f-b8d1811d50e9"
k_range = [2, 5, 7, 10, 15, 20, 25, 30, 40]

silhouette_scores_sampled = []
calinski_scores_sampled = []
davies_bouldin_scores_sampled = []

silhouette_scores = []
calinski_scores = []
davies_bouldin_scores = []

for k_value in k_range:
    model_temp = AgglomerativeClustering(n_clusters=k_value, linkage='ward')
    labels_temp = model_temp.fit_predict(X_sample)

    knn = KNeighborsClassifier(n_neighbors=k_value)
    knn.fit(X_sample, labels_temp)

    labels_full = knn.predict(X_clust_scaled)

    sil_score = silhouette_score(X_clust_scaled, labels_full)
    cal_score = calinski_harabasz_score(X_clust_scaled, labels_full)
    db_score = davies_bouldin_score(X_clust_scaled, labels_full)

    sil_score_sampled = silhouette_score(X_sample, labels_temp)
    cal_score_sampled = calinski_harabasz_score(X_sample, labels_temp)
    db_score_sampled = davies_bouldin_score(X_sample, labels_temp)

    silhouette_scores.append(sil_score)
    calinski_scores.append(cal_score)
    davies_bouldin_scores.append(db_score)

    silhouette_scores_sampled.append(sil_score_sampled)
    calinski_scores_sampled.append(cal_score_sampled)
    davies_bouldin_scores_sampled.append(db_score_sampled)

    print("Sampled")
    print(f"{k_value:<5} {sil_score_sampled:<15.4f} {cal_score_sampled:<20.2f} {db_score_sampled:<20.4f}")
    print("Full")
    print(f"{k_value:<5} {sil_score:<15.4f} {cal_score:<20.2f} {db_score:<20.4f}")

# %% [markdown] id="33B9mFAYYB7g"
# По-детайлен grid search около оптималната стойност на k

# %% id="UNwGFWP9YB7g" outputId="db0f3a54-c071-4d60-ff29-ed36b462b61b"
k_range = [8, 10, 11, 12, 13, 14]

silhouette_scores_sampled = []
calinski_scores_sampled = []
davies_bouldin_scores_sampled = []

silhouette_scores = []
calinski_scores = []
davies_bouldin_scores = []

for k_value in k_range:
    model_temp = AgglomerativeClustering(n_clusters=k_value, linkage='ward')
    labels_temp = model_temp.fit_predict(X_sample)

    knn = KNeighborsClassifier(n_neighbors=k_value)
    knn.fit(X_sample, labels_temp)

    labels_full = knn.predict(X_clust_scaled)

    sil_score = silhouette_score(X_clust_scaled, labels_full)
    cal_score = calinski_harabasz_score(X_clust_scaled, labels_full)
    db_score = davies_bouldin_score(X_clust_scaled, labels_full)

    sil_score_sampled = silhouette_score(X_sample, labels_temp)
    cal_score_sampled = calinski_harabasz_score(X_sample, labels_temp)
    db_score_sampled = davies_bouldin_score(X_sample, labels_temp)

    silhouette_scores.append(sil_score)
    calinski_scores.append(cal_score)
    davies_bouldin_scores.append(db_score)

    silhouette_scores_sampled.append(sil_score_sampled)
    calinski_scores_sampled.append(cal_score_sampled)
    davies_bouldin_scores_sampled.append(db_score_sampled)

    print("Sampled")
    print(f"{k_value:<5} {sil_score_sampled:<15.4f} {cal_score_sampled:<20.2f} {db_score_sampled:<20.4f}")
    print("Full")
    print(f"{k_value:<5} {sil_score:<15.4f} {cal_score:<20.2f} {db_score:<20.4f}")

# %% [markdown] id="NX1h3W5pYB7g"
# След прилагане на Grid Search с метрики Silhouette Score, Calinski–Harabasz и Davies–Bouldin беше избрано k = 10 като оптимален брой клъстери за първото ниво на клъстеризация. Този анализ потвърждава заключенията, направени въз основа на Elbow Method и дендограмата.

# %% id="UDe-23H_YB7g"
k_best = 10
model_final = AgglomerativeClustering(n_clusters=k_best, linkage='ward')
labels_final = model_final.fit_predict(X_sample)

knn = KNeighborsClassifier(n_neighbors=k_best)
knn.fit(X_sample, labels_final)
labels_full = knn.predict(X_clust_scaled)


# %% [markdown] id="l1tLwKGwYB7h"
# Функция за визуализация на разпределението на жанрове по клъстери. Генерира множество графики: bar charts, heatmap и статистики

# %% id="XdnPthxvYB7h"
def visualize_cluster_distribution(df_clust, labels_full, title="Разпределение на жанрове по клъстери", top_n_genres=8):
    cluster_genre_df = pd.DataFrame({
        'cluster': labels_full,
        'genre': df_clust['track_genre'].values
    })

    n_clusters = len(np.unique(labels_full))
    cluster_sizes = pd.Series(labels_full).value_counts().sort_index()

    # Calculate rows needed for subplots (one per cluster + 1 for overview)
    n_rows = (n_clusters + 2) // 2  # +1 for overview, ceil division

    fig, axes = plt.subplots(n_rows, 2, figsize=(16, 4 * n_rows))
    axes = axes.flatten()

    # Plot 1: Cluster sizes overview
    colors_clusters = plt.cm.Set2(np.linspace(0, 1, n_clusters))
    bars = axes[0].bar(cluster_sizes.index, cluster_sizes.values,
                       color=colors_clusters, alpha=0.8, edgecolor='black')
    axes[0].set_title('Размер на клъстерите', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Клъстър', fontsize=12)
    axes[0].set_ylabel('Брой песни', fontsize=12)
    axes[0].grid(axis='y', alpha=0.3)
    for i, v in enumerate(cluster_sizes.values):
        axes[0].text(cluster_sizes.index[i], v + max(cluster_sizes.values)*0.01,
                    f'{v}\n({v/len(labels_full)*100:.1f}%)',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

    # For each cluster: pie chart showing top genres + "Other"
    for idx, cluster_id in enumerate(sorted(np.unique(labels_full))):
        ax = axes[idx + 1]
        cluster_mask = labels_full == cluster_id
        genres_in_cluster = cluster_genre_df[cluster_mask]['genre'].value_counts()

        # Get top genres for this cluster
        top_genres_cluster = genres_in_cluster.head(top_n_genres)
        other_count = genres_in_cluster.iloc[top_n_genres:].sum() if len(genres_in_cluster) > top_n_genres else 0

        # Create data for pie chart
        if other_count > 0:
            pie_data = pd.concat([top_genres_cluster, pd.Series({'Други': other_count})])
        else:
            pie_data = top_genres_cluster

        # Colors: distinct for genres, gray for "Other"
        colors = plt.cm.tab10(np.linspace(0, 1, len(pie_data) - (1 if other_count > 0 else 0)))
        if other_count > 0:
            colors = list(colors) + [(0.7, 0.7, 0.7, 1.0)]  # Gray for "Other"

        wedges, texts, autotexts = ax.pie(
            pie_data.values,
            labels=None,
            autopct=lambda pct: f'{pct:.1f}%' if pct > 5 else '',
            colors=colors,
            startangle=90,
            pctdistance=0.75
        )

        # Add legend with genre names and counts
        legend_labels = [f'{genre}: {count} ({count/cluster_sizes[cluster_id]*100:.1f}%)'
                        for genre, count in pie_data.items()]
        ax.legend(wedges, legend_labels, loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)

        # Dominant genre
        dominant_genre = genres_in_cluster.index[0]
        dominant_pct = genres_in_cluster.iloc[0] / cluster_sizes[cluster_id] * 100

        ax.set_title(f'Клъстър {cluster_id} (n={cluster_sizes[cluster_id]})\nДоминиращ: {dominant_genre} ({dominant_pct:.1f}%)',
                    fontsize=11, fontweight='bold')

    # Hide unused axes
    for idx in range(n_clusters + 1, len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    plt.show()

    print(f"\n{'='*60}")
    print(f"СТАТИСТИКА ЗА КЛЪСТЕРИТЕ")
    print(f"{'='*60}")
    print(f"\nБрой клъстери: {len(np.unique(labels_full))}")
    print(f"Брой уникални жанра: {df_clust['track_genre'].nunique()}")
    print(f"Общо песни: {len(labels_full)}")

    print(f"\n{'='*60}")
    for cluster_id in sorted(np.unique(labels_full)):
        cluster_mask = labels_full == cluster_id
        genres = cluster_genre_df[cluster_mask]['genre'].value_counts()
        print(f"\nКлъстър {cluster_id} ({cluster_sizes[cluster_id]} песни):")
        for genre, count in genres.items():
            pct = (count / cluster_sizes[cluster_id]) * 100
            print(f"  - {genre}: {count} ({pct:.1f}%)")


# %% id="NvoUNXT6YB7h" outputId="bb67d5e3-4bf9-4a1f-fba3-02ef46122da0"
visualize_cluster_distribution(df_clust, labels_full)

# %% [markdown] id="nfmx1SeEYB7h"
# ### Интерпретация на резултатите и йерархична под-клъстеризация
#
# Анализът показа, че изборът на **k=10 клъстера** е добро стратегическо решение. Алгоритъмът успешно разпозна десет отчетливи групи с различни звукови профили: High-BPM Electronic, Global Party, Warm & Regional (бразилска музика), Emotional Ballad, Speech/Comedy, Pure Calm (ambient/sleep), Manic Energy, Groove, Background/Study и смесена група "Wall of Sound".
#
# Тъй като някои клъстери (особено Cluster 0 и Cluster 2) останаха твърде големи, приложихме **йерархична под-клъстеризация**: запазихме първото ниво и приложихме AgglomerativeClustering повторно само върху големите клъстери. Това позволи да разделим огромните групи на по-точни под-категории, без да нарушаваме структурата на останалите добре обособени клъстери.
#
# Аналогичният подход ще бъде приложен и при следващото ниво на клъстеризация („клъстъриране на клъстъри“). Тъй като методологията е идентична с вече описаната при първичното клъстериране, тук няма да се повтаря детайлно. В този раздел ще бъдат представени единствено получените резултати.

# %% [markdown] id="DsFGKnm_YB7h"
# ### Описание на клъстерите (първо ниво)
#
# #### Клъстер 0: „Стената от звук“ (*The Wall of Sound*) — ~28k песни  
# ➡ Подлежи на повторна клъстеризация (re-cluster)
#
# ---
#
# #### Клъстер 1: „Машината с висок BPM“ (*The High-BPM Machine*) — ~11k песни  
#
# **Жанрове:** Techno, Grindcore, Black Metal, DnB  
#
# **Логика:**  
# Този клъстер е доминиран от темпо (скорост). Grindcore и Techno например са изключително бързи жанрове (160+ BPM). Основният обединяващ фактор тук е високата енергия и екстремното темпо.
#
# ---
#
# #### Клъстер 2: „Глобалното парти“ (*The Global Party*) — ~27k песни  
# ➡ Подлежи на повторна клъстеризация (re-cluster)
#
# ---
#
# #### Клъстер 3: „Топло и регионално“ (*Warm & Regional*) — ~6.5k песни  
#
# **Жанрове:** Pagode, Sertanejo, Samba, Gospel, MPB  
#
# **Логика:**  
# Клъстерът улавя специфично бразилско и „топло“ звучене. Тези жанрове споделят сходни перкусионни и вокални характеристики. Получава се изненадващо кохерентно културно групиране.
#
# ---
#
# #### Клъстер 4: „Емоционалната балада“ (*The Emotional Ballad*) — ~18k песни  
#
# **Жанрове:** Romance, Jazz, Opera, Acoustic, Folk  
#
# **Логика:**  
# Ниска енергия, висока акустичност и фокус върху вокалите.  
# Подходящ за сценарии тип *Dinner* или *Date Night*.
#
# ---
#
# #### Клъстер 5: „Клъстерът на речта“ (*The Speech Bucket*) — ~850 песни  
#
# ➡ Около 90% комедия — този клъстер се изключва от обучението върху музикални данни.
#
# ---
#
# #### Клъстер 6: „Чисто спокойствие“ (*Pure Calm*) — ~4.5k песни  
#
# **Предназначение:** Сън / медитация  
#
# **Жанрове:** New-age, Ambient, Piano, Classical  
#
# **Логика:**  
# Без отчетлив ритъм, висока инструменталност и ниска енергия.
#
# ---
#
# #### Клъстер 7: „Маниакална енергия“ (*Manic Energy*) — ~9.8k песни  
#
# **Жанрове:** Happy, Hardstyle, Punk, J-Idol, Metalcore  
#
# **Логика:**  
# Подобен на клъстер 0, но с по-висока валентност (положителност) и по-високо BPM.  
# Може да се опише като „агресия с позитивен заряд“, за разлика от по-мрачния характер на клъстер 0.
#
# ---
#
# #### Клъстер 8: „Груувът“ (*The Groove*) — ~3.5k песни  
#
# **Жанрове:** J-Dance, Dancehall, Funk, Kids  
#
# **Логика:**  
# Силен ритмичен груув и „bounce“ усещане. Ясно разграничим от „flow“ характера на клъстер 2.
#
# ---
#
# #### Клъстер 9: „Фоновата музика“ (*The Background*) — ~3.1k песни  
#
# **Предназначение:** Работа / учене  
#
# **Жанрове:** Study, Guitar, IDM, Chill
#

# %% [markdown] id="brw8G4FeYB7i"
# ### Под-клъстеризация на Cluster 0 (първия голям клъстер - "The Wall of Sound")

# %% id="o_NxYyysYB7i"
df_clust['cluster_1_layer'] = labels_full
X_clust_0 = X_clust_scaled[df_clust['cluster_1_layer'] == 0]

# %% id="KxhLiHrDYB7i"
linked_cluster_0 = linkage(X_clust_0, method='ward')


# %% id="kfit_aThYB7i"
def plot_dendrogram_and_elbow(linked, last_number_of_distances=50, p=8, title_suffix=""):
    last = linked[-last_number_of_distances:, 2]
    last_rev = last[::-1]

    idxs = np.arange(1, len(last) + 1)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    dendrogram(linked, truncate_mode='level', p=p, ax=axes[0])
    axes[0].set_title(f"Hierarchical Clustering Dendrogram {title_suffix} (Ward Linkage)")

    axes[1].plot(idxs, last_rev, label='Ward Distances')
    axes[1].set_title(f'Elbow Method за избор на k {title_suffix}')
    axes[1].set_xlabel('Брой клъстери (k)')
    axes[1].set_ylabel('Разстояние (Ward linkage cost)')
    axes[1].grid(True)

    plt.show()


# %% id="qLDmkUCxYB7i" outputId="22c65e87-ed0d-4458-d032-462a62698e78"
plot_dendrogram_and_elbow(linked_cluster_0, last_number_of_distances=30, p=4, title_suffix="(Cluster 0)")


# %% id="jVuNufbgYB7i"
def grid_search_agglomerative(X_clust, k_range):
    silhouette_scores = []
    calinski_scores = []
    davies_bouldin_scores = []

    print(f"{'k':<5} {'Silhouette':<15} {'Calinski-Harabasz':<20} {'Davies-Bouldin':<20}")
    for k_value in k_range:
        model = AgglomerativeClustering(n_clusters=k_value, linkage='ward')
        labels_full = model.fit_predict(X_clust)

        sil_score = silhouette_score(X_clust, labels_full)
        cal_score = calinski_harabasz_score(X_clust, labels_full)
        db_score = davies_bouldin_score(X_clust, labels_full)

        silhouette_scores.append(sil_score)
        calinski_scores.append(cal_score)
        davies_bouldin_scores.append(db_score)

        print(f"{k_value:<5} {sil_score:<15.4f} {cal_score:<20.2f} {db_score:<20.4f}")


# %% id="4ux2O8gnYB7i" outputId="88d31cd6-7a2d-4b1c-b72d-ac3f1b4d06ea"
k = [4, 5, 6, 7, 8]

grid_search_agglomerative(X_clust_0, k)

# %% id="fpph1ODxYB7i"
k_cluster_0 = 4

# %% id="9V9Uem5YYB7j"
model_clust_0 = AgglomerativeClustering(n_clusters=k_cluster_0, linkage='ward')
labels_clust_0 = model_clust_0.fit_predict(X_clust_0)

# %% id="MQF3ul5HYB7j" outputId="58bd334d-0b59-49a5-bec0-5d4800181b5d"
visualize_cluster_distribution(df_clust[df_clust['cluster_1_layer'] == 0], labels_clust_0)

# %% [markdown] id="g_CQR7VyYB7j"
# #### Sub-Cluster 0: „Bass & Anthems“ – смесена група — 7,074 песни  
#
# **Основни жанрове:** Dubstep, World Music, Gospel, Dub, Mandopop  
#
# **Анализ:**  
# Най-странната група от всички — например Gospel и Dubstep в един и същи клъстер 🙂  
# Вероятно тук моделът улавя общи характеристики в баса или вокалната структура, вместо жанрова близост.
#
# ---
#
# #### Sub-Cluster 1: „Чистият Metal Pit“ (*Pure Metal Pit*) — 9,102 песни  
#
# **Основни жанрове:** Metalcore, Death Metal, Heavy Metal, Grunge, Industrial, Punk  
#
# **Анализ:**  
# Този подклъстер обхваща почти цялата китарно-базирана агресивна музика. „Електронният“ шум тук е почти напълно елиминиран — остава чиста тежка енергия.
#
# ---
#
# #### Sub-Cluster 2: „Club House“ — 6,717 песни  
#
# **Основни жанрове:** Deep House, House, EDM, Electro, Latino, Reggaeton  
#
# **Анализ:**  
# Този подклъстер представя електронната музика със „стабилен бийт“ — танцувален 4-on-the-floor ритъм, обикновено около 120–128 BPM.  
# Успешно отделя *Pop/Dance* енергията от агресивните жанрове.
#
# ---
#
# #### Sub-Cluster 3: „Mainstage Rave“ — 5,212 песни  
#
# **Основни жанрове:** Progressive House, Hardstyle, Trance, Party, EDM  
#
# **Анализ:**  
# Ясно разграничим от Sub-Cluster 2. Докато Sub-Cluster 2 е по-груув ориентиран (Deep House), тук доминират бързи и агресивни стилове като Hardstyle и Trance.  
# Това може да се разглежда като електронния еквивалент на Heavy Metal.
#

# %% [markdown] id="KnGZw882YB7j"
# ### Под-клъстеризация на Cluster 2 (втория голям клъстер - "The Global Party")

# %% id="R-LB7hH9YB7j"
X_clust_2 = X_clust_scaled[df_clust['cluster_1_layer'] == 2]

# %% id="JIpMhXN1o70y"
linkage_clust_2 = linkage(X_clust_2, method='ward')

# %% id="OBRLvNGhYB7j" outputId="843efb54-0b98-4e91-e26b-119a432bbed6"
plot_dendrogram_and_elbow(linkage_clust_2, last_number_of_distances=20, p=5, title_suffix="(Cluster 2)")

# %% id="UvVklY2TYB7j" outputId="6078b8a2-a0fe-4596-bd8e-bf7395c352a8"
k = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

grid_search_agglomerative(X_clust_2, k)

# %% id="9lDxk8IkYB7k" outputId="e67ab27f-3aab-4120-92a9-489a94dc923a"
k = [12, 13, 14]

grid_search_agglomerative(X_clust_2, k)

# %% id="-puCnu9lYB7k"
k_cluster_2 = 4

# %% id="AyaB04ilYB7k"
model_clust_2 = AgglomerativeClustering(n_clusters=k_cluster_2, linkage='ward')
labels_clust_2 = model_clust_2.fit_predict(X_clust_2)

# %% id="-CjS9NHKYB7k" outputId="9f0d7223-a8b3-42be-e7d2-abc782bedb64"
visualize_cluster_distribution(df_clust[df_clust['cluster_1_layer'] == 2], labels_clust_2)

# %% [markdown] id="zahzetS3YB7k"
# #### Sub-Cluster 0: „Mainstream Radio“ — 15,140 песни  
#
# **Основни жанрове:** Party, Disco, Latin-Pop, House, Synth-pop, K-Pop  
#
# **Анализ:**  
# Този подклъстер представя типичното „поп радио“ звучене. Силно разчита на синтезатори, drum machines и стандартен 4/4 ритъм.  
# Дори рок парчетата тук (Alt-Rock, Power-Pop) са по-скоро полирани и ориентирани към масовата аудитория.
#
# ---
#
# #### Sub-Cluster 1 & 2: „Органичните ритми“ (*The Organic Rhythms*) — общо 9,359 песни  
#
# **Основни жанрове:** Salsa, Forró, Rockabilly, Bluegrass, Samba, Rock-n-roll  
#
# **Вибрация:** Акустични барабани, духови инструменти, китари, swing  
#
# **Анализ:**  
# Това е изключително важна сегментация. Алгоритъмът открива, че Rockabilly (50-те години) и Salsa (латино) споделят ключова характеристика: сложни, синкопирани, „човешки“ ритми.  
# Тези жанрове *swing*-ват и *groove*-ват — те не са квантизирани по същия начин като поп музиката в Sub-Cluster 0.
#
# ---
#
# #### Sub-Cluster 3: „Urban Beat“ — 2,629 песни  
#
# **Основни жанрове:** Dancehall, Reggaeton, Hip-Hop, Reggae, J-Dance  
#
# **Вибрация:** Доминиращ бас, Dembow ритми  
#
# **Анализ:**  
# Този подклъстер улавя типичното „urban“ звучене. Различава се ясно от Disco (Cluster 0) поради структурата на бийта (broken beats, dembow ритми) и силния акцент върху sub-bass честотите.
#

# %% [markdown] id="LI2ENNlDYB7k"
# ### Под-клъстеризация на Cluster 4 (втория голям клъстер - "The Emotional Ballad")

# %% id="CyG7OCJDYB7k"
X_clust_4 = X_clust_scaled[df_clust['cluster_1_layer'] == 4]

# %% id="PBmVPSjbpEu7"
linkage_clust_4 = linkage(X_clust_4, method='ward')

# %% id="dcMtWBuzYB7l" outputId="4a69745c-0bc6-4854-ae1f-f1e73f1228cb"
plot_dendrogram_and_elbow(linkage_clust_4, last_number_of_distances=20, p=5, title_suffix="(Cluster 4)")

# %% id="V5rgTX22YB7l" outputId="35eb127c-f95a-4a2a-e6ea-8888577b6e8e"
k = [3, 4, 5, 6, 7, 8, 9]

grid_search_agglomerative(X_clust_4, k)

# %% id="iRyr4Wu-YB7l"
k_cluster_4 = 3

# %% id="OH3puRQtYB7l"
model_clust_4 = AgglomerativeClustering(n_clusters=k_cluster_4, linkage='ward')
labels_clust_4 = model_clust_4.fit_predict(X_clust_4)

# %% id="Aq5dyxAmYB7l" outputId="f7c66746-c00c-4d69-eafa-cab8ccfc6226"
visualize_cluster_distribution(df_clust[df_clust['cluster_1_layer'] == 4], labels_clust_4)

# %% [markdown] id="GpF8bfNhYB7l"
# #### Sub-Cluster 1: „Голямата сцена“ (*The Grand Stage*) — 3,946 песни  
#
# **Основни жанрове:** Opera (9.8%), Show-tunes (5.0%), Disney, Romance  
#
# **Вибрация:** Театрална, оркестрова, драматична.
#
# ---
#
# #### Sub-Cluster 0: „Глобалното акустично кафе“ (*The Global Acoustic Cafe*) — 12,046 песни  
#
# **Основни жанрове:** Tango, Honky-Tonk, Jazz, Mandopop, Acoustic, Singer-Songwriter  
#
# **Вибрация:** Мека, вокално-ориентирана, регионална.  
#
# **Анализ:**  
# Това представлява основното тяло на сантименталната музика. Комбинира „западно“ меко звучене (Jazz, Folk) с „източно/латино“ меко звучене (Mandopop, Tango), което води до културно разнообразен, но емоционално хомогенен клъстер.
#
# ---
#
# #### Sub-Cluster 2: „Средната зона“ (*The Middle Ground*) — 2,470 песни  
# *(подходящ за сливане със Sub-Cluster 0)*  
#
# **Основни жанрове:** Opera (4.5%), Romance, Cantopop, Bluegrass  
#
# **Вибрация:** Нееднозначна.
#
# **Анализ:**  
# Този подклъстер няма ясно изразена идентичност и стои между театралния характер на Sub-Cluster 1 и акустично-сантименталния профил на Sub-Cluster 0, поради което е логично да бъде обединен със Sub-Cluster 0.
#

# %% [markdown] id="5nZFCRsLYB7l"
# Някои от подкластерите се явяват високоподобни помежду си, както по използваните музикални жанрове, така и по емоционалния и акустичен профил, което налага тяхното обединяване с цел постигане на по-ясна и хомогенна класификация. Това е резултат:

# %% [markdown] id="WZpg32WtYB7m"
# | Super Class | Name | Composition (Source) | Sonic Profile |
# |------------|------|---------------------|---------------|
# | Class 1 | HEAVY & AGGRESSIVE | Cluster 0 (Sub 1) + Cluster 7 | Distorted Guitars, High Energy, Screaming Vocals. (Metal, Punk, Grunge). |
# | Class 2 | HIGH-VOLTAGE ELECTRONIC | Cluster 0 (Sub 3) + Cluster 1 | Synthetic, Fast, Repetitive, Aggressive. (Techno, Trance, Hardstyle, DnB). |
# | Class 3 | CLUB & MODERN POP | Cluster 0 (Sub 2) + Cluster 2 (Sub 0) | 4/4 Beats, Polished Production, Radio Friendly. (House, Disco, Pop, EDM). |
# | Class 4 | URBAN & GROOVE | Cluster 2 (Sub 3) + Cluster 8 | Broken Beats, Bass Heavy, Syncopated. (Hip-Hop, Reggaeton, Funk, Dancehall). |
# | Class 5 | ORGANIC & ROOTS | Cluster 2 (Sub 1+2) + Cluster 4 (Sub 0+2) + Cluster 3 | Acoustic Instruments, Human Rhythms, Warm. (Jazz, Folk, Salsa, Country, Samba). |
# | Class 6 | ATMOSPHERIC & DRAMATIC | Cluster 6 + Cluster 9 + Cluster 4 (Sub 1) | Low Energy or Orchestral, Mood-based. (Classical, Opera, Ambient, Study). |

# %% [markdown] id="3cOIgs-MYB7m"
# За оптимизиране на качеството на обучението и повишаване на надеждността на предсказанията, се предприема филтриране на outliers в рамките на всеки клъстер. Към outliers се отнасят жанрови проби с ниска представителност, които не са типични за съответния клъстер. Премахването им осигурява по-хомогенен тренировъчен сет и минимизира риска от въвеждане на шум в моделите за жанрова класификация.

# %% id="XQYhz4yNYB7m"
cluster_to_class = {
    1: 2,  # Cluster 1 -> HIGH-VOLTAGE ELECTRONIC
    7: 1,  # Cluster 7 -> HEAVY & AGGRESSIVE
    8: 4,  # Cluster 8 -> URBAN & GROOVE
    3: 5,  # Cluster 3 -> ORGANIC & ROOTS
    6: 6,  # Cluster 6 -> ATMOSPHERIC & DRAMATIC
    9: 6,  # Cluster 9 -> ATMOSPHERIC & DRAMATIC
    5: -1, # Cluster 5 -> Speech/Comedy (excluded)
}

df_clust['class'] = -1

for cluster_id, class_id in cluster_to_class.items():
    mask = df_clust['cluster_1_layer'] == cluster_id
    df_clust.loc[mask, 'class'] = class_id

mask_c0 = df_clust['cluster_1_layer'] == 0
indices_c0 = df_clust[mask_c0].index
labels_c0_series = pd.Series(labels_clust_0, index=indices_c0)

df_clust.loc[indices_c0[labels_c0_series == 1], 'class'] = 1  # Sub 1 -> HEAVY & AGGRESSIVE
df_clust.loc[indices_c0[labels_c0_series == 3], 'class'] = 2  # Sub 3 -> HIGH-VOLTAGE ELECTRONIC
df_clust.loc[indices_c0[labels_c0_series == 2], 'class'] = 3  # Sub 2 -> CLUB & MODERN POP
df_clust.loc[indices_c0[labels_c0_series == 0], 'class'] = 3  # Sub 0 -> CLUB & MODERN POP (Bass & Anthems)

mask_c2 = df_clust['cluster_1_layer'] == 2
indices_c2 = df_clust[mask_c2].index
labels_c2_series = pd.Series(labels_clust_2, index=indices_c2)

df_clust.loc[indices_c2[labels_c2_series == 0], 'class'] = 3  # Sub 0 -> CLUB & MODERN POP
df_clust.loc[indices_c2[labels_c2_series == 3], 'class'] = 4  # Sub 3 -> URBAN & GROOVE
df_clust.loc[indices_c2[labels_c2_series == 1], 'class'] = 5  # Sub 1 -> ORGANIC & ROOTS
df_clust.loc[indices_c2[labels_c2_series == 2], 'class'] = 5  # Sub 2 -> ORGANIC & ROOTS

mask_c4 = df_clust['cluster_1_layer'] == 4
indices_c4 = df_clust[mask_c4].index
labels_c4_series = pd.Series(labels_clust_4, index=indices_c4)

df_clust.loc[indices_c4[labels_c4_series == 1], 'class'] = 6  # Sub 1 -> ATMOSPHERIC & DRAMATIC
df_clust.loc[indices_c4[labels_c4_series == 0], 'class'] = 5  # Sub 0 -> ORGANIC & ROOTS
df_clust.loc[indices_c4[labels_c4_series == 2], 'class'] = 5  # Sub 2 -> ORGANIC & ROOTS


# %% id="E3335VhrYB7m"
def analyze_genre_distribution(df_clust):
    print("="*80)
    print("РАЗПРЕДЕЛЕНИЕ НА ЖАНРОВЕ ПО КЛАСОВЕ")
    print("="*80)

    class_names = {
        1: "HEAVY & AGGRESSIVE",
        2: "HIGH-VOLTAGE ELECTRONIC",
        3: "CLUB & MODERN POP",
        4: "URBAN & GROOVE",
        5: "ORGANIC & ROOTS",
        6: "ATMOSPHERIC & DRAMATIC"
    }

    for class_id in sorted(df_clust['class'].unique()):
        if class_id == -1:
            print(f"\n{'='*80}")
            print(f"Клас {class_id}: EXCLUDED (Speech/Comedy)")
            print(f"{'='*80}")
        else:
            print(f"\n{'='*80}")
            print(f"Клас {class_id}: {class_names.get(class_id, 'UNKNOWN')}")
            print(f"{'='*80}")

        class_mask = df_clust['class'] == class_id
        class_df = df_clust[class_mask]

        total_songs = len(class_df)
        print(f"\nОбщо песни: {total_songs} ({total_songs/len(df_clust)*100:.2f}% от всички)")

        unique_genres = class_df['track_genre'].nunique()
        print(f"Брой уникални жанрове: {unique_genres}")

        genre_counts = class_df['track_genre'].value_counts()

        print(f"\nТоп 10 жанра:")
        for i, (genre, count) in enumerate(genre_counts.head(10).items(), 1):
            pct = (count / total_songs) * 100
            print(f"  {i:2d}. {genre:20s}: {count:5d} ({pct:5.2f}%)")

        if len(genre_counts) > 10:
            remaining = genre_counts.iloc[10:].sum()
            pct = (remaining / total_songs) * 100
            print(f"  ... Останали {len(genre_counts)-10} жанра: {remaining:5d} ({pct:5.2f}%)")

    print(f"\n{'='*80}")
    print("ОБОБЩЕНА СТАТИСТИКА")
    print(f"{'='*80}")

    summary_data = []
    for class_id in sorted(df_clust['class'].unique()):
        if class_id != -1:
            class_mask = df_clust['class'] == class_id
            class_df = df_clust[class_mask]

            summary_data.append({
                'Class': class_id,
                'Name': class_names.get(class_id, 'UNKNOWN'),
                'Songs': len(class_df),
                'Genres': class_df['track_genre'].nunique(),
                'Percentage': f"{len(class_df)/len(df_clust[df_clust['class'] != -1])*100:.2f}%"
            })

    summary_df = pd.DataFrame(summary_data)
    print(f"\n{summary_df.to_string(index=False)}")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    class_sizes = df_clust[df_clust['class'] != -1]['class'].value_counts().sort_index()
    colors = plt.cm.Set3(np.linspace(0, 1, len(class_sizes)))

    bars = axes[0].bar(class_sizes.index, class_sizes.values, color=colors, alpha=0.8, edgecolor='black')
    axes[0].set_xlabel('Клас', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Брой песни', fontsize=12, fontweight='bold')
    axes[0].set_title('Размер на класовете', fontsize=14, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)

    for i, v in enumerate(class_sizes.values):
        axes[0].text(class_sizes.index[i], v + max(class_sizes.values)*0.01,
                    f'{v}\n({v/len(df_clust[df_clust["class"] != -1])*100:.1f}%)',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    genre_counts_per_class = []
    for class_id in sorted(df_clust[df_clust['class'] != -1]['class'].unique()):
        class_mask = df_clust['class'] == class_id
        genre_counts_per_class.append(df_clust[class_mask]['track_genre'].nunique())

    bars = axes[1].bar(sorted(df_clust[df_clust['class'] != -1]['class'].unique()),
                       genre_counts_per_class, color=colors, alpha=0.8, edgecolor='black')
    axes[1].set_xlabel('Клас', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Брой уникални жанрове', fontsize=12, fontweight='bold')
    axes[1].set_title('Жанрово разнообразие по класове', fontsize=14, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)

    for i, v in enumerate(genre_counts_per_class):
        axes[1].text(sorted(df_clust[df_clust['class'] != -1]['class'].unique())[i],
                    v + max(genre_counts_per_class)*0.01, f'{v}',
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.show()


# %% id="MBh0GeZWYB7m" outputId="bdf70eb2-3ca7-4f86-91b3-0c0467bf1852"
analyze_genre_distribution(df_clust)


# %% id="1D3N4LnCYB7m"
def filter_rare_genres_in_classes(df_clust, min_samples_per_class=50, min_percentage=1.0):
    class_names = {
        1: "HEAVY & AGGRESSIVE",
        2: "HIGH-VOLTAGE ELECTRONIC",
        3: "CLUB & MODERN POP",
        4: "URBAN & GROOVE",
        5: "ORGANIC & ROOTS",
        6: "ATMOSPHERIC & DRAMATIC"
    }

    df_work = df_clust.copy()

    # Exclude class -1 (Speech/Comedy) from filtering
    df_work_valid = df_work[df_work['class'] != -1]

    keep_mask = pd.Series([False] * len(df_work), index=df_work.index)

    stats = {}

    # Track all original genres (excluding class -1)
    all_original_genres = set(df_work_valid['track_genre'].unique())

    for class_id in sorted(df_work_valid['class'].unique()):
        class_mask = df_work['class'] == class_id
        class_data = df_work[class_mask]
        class_size = len(class_data)

        genre_counts = class_data['track_genre'].value_counts()
        threshold_count = max(min_samples_per_class, int(class_size * min_percentage / 100))

        genres_to_keep = genre_counts[genre_counts >= threshold_count].index.tolist()
        genres_removed = genre_counts[genre_counts < threshold_count].index.tolist()

        genre_mask = df_work['track_genre'].isin(genres_to_keep)
        keep_mask = keep_mask | (class_mask & genre_mask)

        kept_songs = class_data[class_data['track_genre'].isin(genres_to_keep)].shape[0]
        removed_songs = class_size - kept_songs

        stats[class_id] = {
            'class_name': class_names.get(class_id, 'UNKNOWN'),
            'original_size': class_size,
            'genres_kept': len(genres_to_keep),
            'genres_removed': len(genres_removed),
            'songs_kept': kept_songs,
            'songs_removed': removed_songs,
            'kept_genres_list': genres_to_keep,
            'removed_genres_list': genres_removed
        }

        print(f"\n{'='*70}")
        print(f"КЛАС {class_id}: {class_names.get(class_id, 'UNKNOWN')} ({class_size} песни)")
        print(f"{'='*70}")
        print(f"  Праг: {threshold_count} примера (min {min_samples_per_class} или {min_percentage}%)")
        print(f"  Жанрове запазени: {len(genres_to_keep)} | Премахнати: {len(genres_removed)}")
        print(f"  Песни запазени: {kept_songs} ({kept_songs/class_size*100:.1f}%)")
        print(f"\n  Запазени жанрове ({len(genres_to_keep)}):")
        for genre in genres_to_keep:
            count = genre_counts[genre]
            pct = count / class_size * 100
            print(f"    - {genre}: {count} ({pct:.1f}%)")
        if genres_removed:
            print(f"\n  Премахнати жанрове ({len(genres_removed)}):")
            for genre in genres_removed[:15]:
                count = genre_counts[genre]
                print(f"    - {genre}: {count}")
            if len(genres_removed) > 15:
                print(f"    ... и още {len(genres_removed) - 15} жанра")

    df_filtered = df_work[keep_mask].copy()

    # Check which genres completely disappeared from the dataset
    remaining_genres = set(df_filtered['track_genre'].unique())
    disappeared_genres = all_original_genres - remaining_genres

    print(f"\n{'='*70}")
    print(f"ОБОБЩЕНИЕ")
    print(f"{'='*70}")
    print(f"  Оригинален размер (без class -1): {len(df_work_valid)}")
    print(f"  Филтриран размер: {len(df_filtered)}")
    print(f"  Премахнати песни: {len(df_work_valid) - len(df_filtered)} ({(len(df_work_valid) - len(df_filtered))/len(df_work_valid)*100:.1f}%)")
    print(f"\n  Оригинални жанрове: {len(all_original_genres)}")
    print(f"  Останали жанрове: {len(remaining_genres)}")
    print(f"  Напълно изчезнали жанрове: {len(disappeared_genres)}")

    if disappeared_genres:
        print(f"\n{'='*70}")
        print(f"ЖАНРОВЕ, КОИТО НАПЪЛНО ИЗЧЕЗНАХА ОТ DATASET-А ({len(disappeared_genres)}):")
        print(f"{'='*70}")
        for genre in sorted(disappeared_genres):
            original_count = df_work_valid[df_work_valid['track_genre'] == genre].shape[0]
            # Find which class(es) this genre was in
            classes_with_genre = df_work_valid[df_work_valid['track_genre'] == genre]['class'].unique()
            classes_str = ', '.join([f"{c} ({class_names.get(c, '?')})" for c in classes_with_genre])
            print(f"  - {genre}: {original_count} песни | Беше в клас(ове): {classes_str}")

    # Add to stats
    stats['_summary'] = {
        'original_genres': len(all_original_genres),
        'remaining_genres': len(remaining_genres),
        'disappeared_genres': list(disappeared_genres),
        'disappeared_count': len(disappeared_genres)
    }

    return df_filtered, stats


# %% colab={"base_uri": "https://localhost:8080/"} id="5CV7k52tYB7n" outputId="cf6bc568-415b-4804-d983-6e00ed85af65"
# Филтриране на редки жанрове в рамките на всеки КЛАС (супер-клас)
df_clust_filtered, filter_stats = filter_rare_genres_in_classes(
    df_clust,
    min_samples_per_class=50,
    min_percentage=1.1
)

# %% [markdown] id="gnJtyVaSYB7n"
# Използваният подход не е оптимален по отношение на запазването на всички налични данни, тъй като в процеса на филтриране бяха загубени значителен брой наблюдения. Въпреки това, остава достатъчно голям обем данни, който позволява ефективно обучение на модела.
#
# Премахването на редките, слабо представени жанрове намалява броя на вътрешноклъстерните шумови класове и подпомага модела да научи по-консистентни и репрезентативни характеристики за всеки клъстер, като по този начин се подобрява качеството на предсказанията.

# %% [markdown] id="iQWqXyrAYB7n"
# # Част 3: Обучение и валидиране на модели чрез използване на супер-класове

# %% [markdown] id="rtCeBCIXYB7n"
# ## Йерархична класификация „разделяй и владей“ (superclass → genre)
#
# Следващият подход използва принципа **„разделяй и владей“**: вместо да обучаваме един единствен модел да разпознава всички жанрове наведнъж, първо групираме жанровете в **предефинирани 6 супер-класа** (получени от клъстеризацията - merge таблицата „по vibe“) и после обучаваме отделни модели **само вътре в съответния супер-клас**.
#
# ### Защо това е добра идея?
# - **Супер-класовете съдържат близки по звучене жанрове**, т.е. в рамките на един супер-клас разграничаването е по-фино и по-структурирано.
# - Вместо моделът да се разсейва от голям брой несвързани жанрове, той решава **по-малка и по-конкретна задача**.
# - Това прави системата по-интерпретируема: можем да кажем *„песента е в vibe-клас X, а вътре в него най-вероятният жанр е Y“*.
#
# ### Какво прави кодът по-долу?
# 1. **Създаваме `df_classified`** – филтрирана версия на оригиналния датафрейм:
#    - оставяме само редовете, които са запазени след филтъра за редки/аномални жанрове (`df_clust_filtered`);
#    - добавяме колоната `class` (супер-клас) към всеки трак;
#    - оставяме само нужните feature колони + `track_genre` и `class`.
#
# 2. **Правим един общ train/test split**, който едновременно пази:
#    - етикета за супер-клас (`class`) – нужен за първи слой;
#    - етикета за жанр (`track_genre`) – нужен за втори слой;
#    - като използваме `stratify` по `class`, за да запазим разпределението на супер-класовете в train/test.
#
# 3. **Първи слой (superclass classifier)**: обучаваме модел, който предсказва кой от 6-те супер-класа е дадена песен.
#    - В кода сравняваме няколко класически и ансамблови модела (kNN, MLP, Logistic Regression, Linear SVM, Random Forest, ExtraTrees, HistGradientBoosting) и избираме най-добрия по macro_f1.
#
# 4. **Втори слой (genre classifier по superclass)**: за всеки супер-клас обучаваме отделен модел, който различава жанровете *само в този супер-клас*.
#    - Понеже жанровете във всеки супер-клас са различни, за всеки супер-клас използваме отделен `LabelEncoder`.
#    - За теста мерим само тези жанрове, които се срещат в train за съответния супер-клас („known genres“), за да няма технически проблеми при преобразуването на етикетите.
#
# 5. **Двустепенно предсказване (end-to-end)**: комбинираме двата слоя: първо предсказваме супер-клас, после подаваме примера на модела за жанр на този супер-клас, накрая оценяваме резултата върху test (точност, macro F1 и coverage).
#
# **Забележка**: Super-class 1 (HEAVY & AGGRESSIVE) е дефиниран на етап клъстеризация, но не участва във фазата на моделиране, тъй като след филтрирането не присъства в използвания за обучение поднабор от данни `df_classified`.
#

# %% [markdown] id="tuFcYwsJEDDP"
# ### Super-classes (vibe групи) от клъстеризацията
#
# | Super Class | Name | Composition (Source) | Sonic Profile |
# |---|---|---|---|
# | Class 1 | HEAVY & AGGRESSIVE | Cluster 0 (Sub 1) + Cluster 7 | Distorted guitars, high energy, screaming vocals (Metal, Punk, Grunge) |
# | Class 2 | HIGH-VOLTAGE ELECTRONIC | Cluster 0 (Sub 3) + Cluster 1 | Synthetic, fast, repetitive, aggressive (Techno, Trance, Hardstyle, DnB) |
# | Class 3 | CLUB & MODERN POP | Cluster 0 (Sub 2) + Cluster 2 (Sub 0) | 4/4 beats, polished production, radio friendly (House, Disco, Pop, EDM) |
# | Class 4 | URBAN & GROOVE | Cluster 2 (Sub 3) + Cluster 8 | Broken beats, bass heavy, syncopated (Hip-Hop, Reggaeton, Funk, Dancehall) |
# | Class 5 | ORGANIC & ROOTS | Cluster 2 (Sub 1+2) + Cluster 4 (Sub 0+2) + Cluster 3 | Acoustic instruments, human rhythms, warm (Jazz, Folk, Salsa, Country, Samba) |
# | Class 6 | ATMOSPHERIC & DRAMATIC | Cluster 6 + Cluster 9 + Cluster 4 (Sub 1) | Low energy / orchestral, mood-based (Classical, Opera, Ambient, Study) |
#

# %% id="MRCoGaqoYB7n"
df_classified = df.copy()

# %% id="FXNaLGavYB7n"
df_classified = df_classified.loc[df_clust_filtered.index]

# %% id="BqrvMK50YB7n"
df_classified['class'] = df_clust_filtered['class']

# %% colab={"base_uri": "https://localhost:8080/", "height": 481} id="4WnEduTeYB7o" outputId="20f7d5d7-01c7-433b-a2ca-e5a5d01aa2cb"
df_classified.head()

# %%
# df_classified.to_csv("classified_songs_dataset.csv", index=False)

# %% colab={"base_uri": "https://localhost:8080/"} id="Cl3FRFooYB7o" outputId="5f51731f-5140-483e-b932-b6cf29226003"
df_classified.shape

# %% colab={"base_uri": "https://localhost:8080/", "height": 206} id="DOJ-olhoYB7o" outputId="73f9da7e-49b4-4088-f9da-188b83d1e427"
df_classified = df_classified[feature_cols + [target_col, 'class']].copy()
df_classified.drop(['popularity', 'duration_ms'], axis=1, inplace=True)
df_classified.head()

# %%
df_classified.describe()

# %%
from sklearn.preprocessing import StandardScaler

# %% id="RuUfOwugYB7o"
features_superclass = df_classified[audio_features].values
features_genre = df_classified.drop(['track_genre', 'class'], axis=1).values

superclass_labels = df_classified["class"].values
genre_labels = df_classified["track_genre"].values

indices = np.arange(len(df_classified))

train_idx, test_idx, superclass_train, superclass_test = train_test_split(
    indices,
    superclass_labels,
    test_size=0.2,
    random_state=42,
    stratify=superclass_labels
)

X_train_superclass = features_superclass[train_idx]
X_test_superclass = features_superclass[test_idx]

X_train_genre = features_genre[train_idx]
X_test_genre = features_genre[test_idx]

genre_train = genre_labels[train_idx]
genre_test = genre_labels[test_idx]

scaler_superclass = StandardScaler()
X_train_superclass = scaler_superclass.fit_transform(X_train_superclass)
X_test_superclass = scaler_superclass.transform(X_test_superclass)

scaler_genre = StandardScaler()
X_train_genre = scaler_genre.fit_transform(X_train_genre)
X_test_genre = scaler_genre.transform(X_test_genre)

print(f"Train size: {len(train_idx)}, Test size: {len(test_idx)}")
print(f"Superclass features shape: {X_train_superclass.shape}")
print(f"Genre features shape: {X_train_genre.shape}")
print("Data scaled with StandardScaler")

# %%
# !pip install catboost

# %% id="EzPY2hZHrvkZ"
from catboost import CatBoostClassifier

def make_candidate_models(random_state=67):
    return {
        "mlp": MLPClassifier(
            hidden_layer_sizes=(128, 64),
            max_iter=800,
            early_stopping=True,
            n_iter_no_change=10,
            random_state=random_state
        ),

        "knn": KNeighborsClassifier(n_neighbors=15, n_jobs=1),

        "logreg": LogisticRegression(
            max_iter=2000,
            n_jobs=1,
            class_weight="balanced",
            random_state=random_state
        ),

        "linsvc": LinearSVC(
            class_weight="balanced",
            random_state=random_state
        ),

        "rf": RandomForestClassifier(
            n_estimators=400,
            random_state=random_state,
            n_jobs=1,
            class_weight="balanced_subsample"
        ),

        "xgb": XGBGenreClassifier(
            n_estimators=300,
            max_depth=8,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=random_state,
            n_jobs=1
        ),

        "extratrees": ExtraTreesClassifier(
            n_estimators=600,
            random_state=random_state,
            n_jobs=1,
            class_weight="balanced_subsample"
        ),

        "hgb": HistGradientBoostingClassifier(
            max_depth=None,
            learning_rate=0.1,
            max_iter=300,
            random_state=random_state
        ),

        "catboost": CatBoostClassifier(
            iterations=500,
            learning_rate=0.1,
            depth=8,
            random_seed=random_state,
            verbose=0,
            auto_class_weights="Balanced",
            thread_count=1
        )
    }


# %% id="8mjFyzp1rx4E"
def evaluate_model(model, X_eval, y_eval):
    pred = model.predict(X_eval)
    return {
        "acc": accuracy_score(y_eval, pred),
        "macro_f1": f1_score(y_eval, pred, average="macro")
    }


# %% id="GenHhj6nrzlW"
def choose_best_model(candidates, X_train_local, y_train_local, X_eval, y_eval, pick_metric="macro_f1"):
    best_name, best_model, best_score, best_metrics = None, None, -1.0, None

    for name, model in candidates.items():
        model.fit(X_train_local, y_train_local)
        metrics = evaluate_model(model, X_eval, y_eval)
        score = metrics[pick_metric]

        if score > best_score:
            best_name, best_model, best_score, best_metrics = name, model, score, metrics

    return best_name, best_model, best_metrics


# %% colab={"base_uri": "https://localhost:8080/"} id="QQcDwqSVr2Je" outputId="3b76df8f-fd2e-459d-8018-1e9e95a75197"
# Първи слой: модел за superclass (6 класа)
superclass_candidates = make_candidate_models()
best_superclass_name, superclass_model, superclass_metrics = choose_best_model(
    superclass_candidates,
    X_train_superclass, superclass_train,
    X_test_superclass, superclass_test,
    pick_metric="macro_f1"
)

print(f"[SUPERCLASS] best={best_superclass_name} | acc={superclass_metrics['acc']:.4f} | macro_f1={superclass_metrics['macro_f1']:.4f}")

# %% colab={"base_uri": "https://localhost:8080/"} id="-TguiSVlH4Ej" outputId="8895fcca-f60c-4e9a-a640-db86c87e07e3"
df_classified["class"].isna().sum(), (df_classified["class"] == -1).sum(), df_classified["class"].value_counts(dropna=False).head(10)


# %% [markdown] id="_L50McS-pRFQ"
# #### Randomized Search за втори слой (genre) по superclass (само за най-добрия модел)
#
# За всеки `superclass` първо избираме **най-силния модел** спрямо `Macro F1` върху отделения test поднабор за този superclass.
# След това правим **Randomized Search (CV върху train частта за този superclass)** *само* за избрания модел, за да оптимизираме хиперпараметрите му.
# Накрая оценяваме **tuned** модела върху `test_known` (жанрове, които се срещат и в train), за да сравним преди/след.

# %% id="Xf5iQa7BpVMR"
from sklearn.model_selection import RandomizedSearchCV
from sklearn.base import clone
import numpy as np
from scipy.stats import uniform, randint, loguniform
import os


PARAM_GRIDS = {
    "knn": {
        "n_neighbors": [5, 11, 15, 21],  
        "weights": ["distance"],  
        "metric": ["manhattan", "euclidean"],  
        "p": [1, 2]
    },
    
    "logreg": {
        "C": [0.1, 1.0, 10.0, 50.0],
        "penalty": ["l2"],
        "solver": ["lbfgs"],
        "max_iter": [2000]     
    },
    
    "linsvc": {
        "C": [0.5, 1.0, 5.0, 10.0],
        "loss": ["squared_hinge"],  
        "max_iter": [2000]
    },
    
    "mlp": {
        "hidden_layer_sizes": [(256,), (128,), (256, 128), (128, 64)],
        "alpha": [1e-4, 1e-3, 1e-2],  
        "learning_rate_init": [0.001, 0.0005],
        "learning_rate": ["adaptive"],
        "activation": ["relu"],
        "batch_size": [128, 256]
    },
    
    "rf": {
        "n_estimators": [200, 300, 500],
        "max_depth": [20, 30, None],  
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
        "max_features": ["sqrt", "log2"],  
        "class_weight": ["balanced_subsample"],
        "bootstrap": [True]
    },
    
    "extratrees": {
        "n_estimators": [200, 400, 600],
        "max_depth": [25, 35, None],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2],
        "max_features": ["sqrt"],
        "class_weight": ["balanced_subsample"],
        "bootstrap": [False]
    },
    
    "hgb": {
        "learning_rate": [0.05, 0.1, 0.15],
        "max_iter": [200, 300, 500],
        "max_depth": [8, 12, None],
        "min_samples_leaf": [15, 20],
        "l2_regularization": [0.0, 0.1],
        "max_bins": [255]
    },
    
    "xgb": {
        "n_estimators": [200, 300, 500],
        "max_depth": [6, 8, 10],
        "learning_rate": [0.05, 0.1],
        "subsample": [0.8, 0.9],
        "colsample_bytree": [0.8, 0.9],
        "reg_lambda": [1, 2]
    },
    
    "catboost": {
        "iterations": [300, 500, 700],
        "learning_rate": [0.05, 0.1],
        "depth": [6, 8, 10],
        "l2_leaf_reg": [3, 5],
        "border_count": [128, 254],
        "bagging_temperature": [0.5, 1.0],
        "random_strength": [1]
    }
}

def safe_cv_splits(y, max_cv=3):
    y = np.asarray(y)
    counts = np.bincount(y) if y.dtype.kind in "iu" else None
    if counts is None or len(counts) == 0:
        return 2
    min_count = counts[counts > 0].min()
    cv = min(max_cv, int(min_count))
    return cv if cv >= 2 else 0

def grid_search_best_only(best_name, candidates, X_tr, y_tr, scoring="f1_macro", n_jobs=5, n_iter=15):
    if best_name not in PARAM_GRIDS:
        return None, None

    cv = safe_cv_splits(y_tr, max_cv=3)
    if cv < 2:
        return None, None

    est = clone(candidates[best_name])
    rs = RandomizedSearchCV(
        estimator=est,
        param_distributions=PARAM_GRIDS[best_name],
        n_iter=n_iter,
        scoring=scoring,
        cv=cv,
        refit=True,
        random_state=42,
        n_jobs=n_jobs,
        verbose=0
    )
    rs.fit(X_tr, y_tr)
    return rs.best_estimator_, rs.best_params_


# %% colab={"base_uri": "https://localhost:8080/"} id="hxcPlWWer7IY" outputId="cb2250a4-8ca4-41f0-9ec9-07d2e1ebb2ec"
# Втори слой: модел за genre във всеки superclass
# - тренираме отделен модел за всеки superclass
# - отделен LabelEncoder за жанровете вътре в този superclass
genre_model_by_superclass = {}
genre_encoder_by_superclass = {}
genre_best_params_by_superclass = {}
genre_metrics_by_superclass = {}

unique_superclasses = sorted(np.unique(superclass_train))

for sc in unique_superclasses:
    train_in_sc = (superclass_train == sc)
    test_in_sc = (superclass_test == sc)

    train_features_sc = X_train_genre[train_in_sc]
    test_features_sc = X_test_genre[test_in_sc]

    train_genres_sc = np.array(genre_train)[train_in_sc]
    test_genres_sc = np.array(genre_test)[test_in_sc]

    # Ако класът е твърде малък, няма да има смисъл и стабилност
    if len(train_features_sc) < 200:
        continue

    genre_encoder = LabelEncoder()
    train_genre_ids_sc = genre_encoder.fit_transform(train_genres_sc)

    # Ако в този superclass има само 1 жанр -> няма класификация
    if len(genre_encoder.classes_) < 2:
        continue

    # Тест: взимаме само жанровете, които се срещат в train (за да не се чупи encoder)
    test_genre_is_known = np.isin(test_genres_sc, genre_encoder.classes_)
    test_features_known = test_features_sc[test_genre_is_known]
    test_genre_ids_known = genre_encoder.transform(test_genres_sc[test_genre_is_known])

    # Ако нямаме никакви валидни test примери, пак може да тренираме, но няма какво да мерим
    genre_candidates = make_candidate_models()
    best_genre_name, best_genre_model, best_genre_metrics = choose_best_model(
        genre_candidates,
        train_features_sc, train_genre_ids_sc,
        test_features_known, test_genre_ids_known,
        pick_metric="macro_f1"
    ) if len(test_features_known) > 0 else (None, None, None)

    # ---- GRID SEARCH (само за най-добрия модел) ----
    tuned_model = None
    tuned_params = None
    tuned_metrics = best_genre_metrics

    if len(test_features_known) > 0 and best_genre_name is not None:
        tuned_model, tuned_params = grid_search_best_only(
            best_name=best_genre_name,
            candidates=genre_candidates,
            X_tr=train_features_sc,
            y_tr=train_genre_ids_sc,
            scoring="f1_macro",
        )

        # ако grid search е минал успешно -> оценяваме tuned модела върху test_known
        if tuned_model is not None:
            tuned_metrics = evaluate_model(tuned_model, test_features_known, test_genre_ids_known)
            best_genre_model = tuned_model
            best_genre_name = f"{best_genre_name}+RS"

    genre_best_params_by_superclass[int(sc)] = tuned_params

    # Ако няма тест за мерене, просто тренираме с предпочитан модел
    if best_genre_model is None:
        best_genre_name = "rf"
        best_genre_model = make_candidate_models()["rf"]
        best_genre_model.fit(train_features_sc, train_genre_ids_sc)
        best_genre_metrics = {"acc": np.nan, "macro_f1": np.nan}

    genre_model_by_superclass[int(sc)] = best_genre_model
    genre_encoder_by_superclass[int(sc)] = genre_encoder
    genre_metrics_by_superclass[int(sc)] = (best_genre_name, best_genre_metrics, len(genre_encoder.classes_), len(train_features_sc), len(test_features_known))

    print(f"[GENRE | sc={sc}] best={best_genre_name} | acc={best_genre_metrics['acc']:.4f} | macro_f1={best_genre_metrics['macro_f1']:.4f} "
          f"| genres={len(genre_encoder.classes_)} | train={len(train_features_sc)} | test_known={len(test_features_known)}")


# %% id="f_nOxziHq6RO"
def predict_two_stage(features_superclass, features_array):
    predicted_superclasses = superclass_model.predict(features_superclass)
    predicted_genres = []

    for i, sc in enumerate(predicted_superclasses):
        sc = int(sc)

        if sc not in genre_model_by_superclass:
            predicted_genres.append(None)
            continue

        model = genre_model_by_superclass[sc]
        encoder = genre_encoder_by_superclass[sc]

        predicted_genre_id = int(model.predict(features_array[i:i+1])[0])
        predicted_genres.append(encoder.inverse_transform([predicted_genre_id])[0])

    return predicted_superclasses, np.array(predicted_genres, dtype=object)


# %% colab={"base_uri": "https://localhost:8080/"} id="PH0o3vewrD-N" outputId="e13c48da-4aba-410d-f026-1149eee873c6"
pred_super_test, pred_genre_test = predict_two_stage(X_test_superclass, X_test_genre)

print(f"[E2E SUPERCLASS] acc={accuracy_score(superclass_test, pred_super_test):.4f} | macro_f1={f1_score(superclass_test, pred_super_test, average='macro'):.4f}")

has_genre_pred = pred_genre_test != None
if has_genre_pred.sum() > 0:
    e2e_genre_acc = accuracy_score(np.array(genre_test)[has_genre_pred], pred_genre_test[has_genre_pred])
    e2e_genre_f1 = f1_score(np.array(genre_test)[has_genre_pred], pred_genre_test[has_genre_pred], average="macro")
    print(f"[E2E GENRE] coverage={has_genre_pred.mean():.3f} | acc={e2e_genre_acc:.4f} | macro_f1={e2e_genre_f1:.4f}")

# %% colab={"base_uri": "https://localhost:8080/", "height": 175} id="f7FubyeO1tBH" outputId="d9c356b2-cc4d-44f5-ef68-f598d622f37f"
rows = []

for sc, (model_name, metrics, n_genres, n_train, n_test) in genre_metrics_by_superclass.items():
    rows.append({
        "layer": f"genre | sc={sc}",
        "model": model_name,
        "acc": metrics["acc"],
        "macro_f1": metrics["macro_f1"],
        "genres": n_genres,
        "train_samples": n_train,
        "test_known": n_test
    })

summary_df = pd.DataFrame(rows)
summary_df

# %% [markdown] id="qB7EzE1wwZt0"
# ## Интерпретация на резултатите (след добавяне на нови модели)
#
# ### 1) Първи слой: предсказване на супер-клас (6 vibe класа)
# Най-добрият модел за първия слой остава **kNN**, с:
# - **Accuracy = 0.9606**
# - **Macro F1 = 0.9474**
#
# Това показва, че **супер-класовете са добре разделими** по използваните аудио характеристики и системата надеждно определя „vibe" групата на дадена песен. Високият macro F1 подсказва, че резултатът е стабилен и не зависи само от най-големия супер-клас.
#
# ### 2) Втори слой: предсказване на жанр вътре в супер-клас
# За втория слой наблюдаваме различно поведение според супер-класа:
#
# - **sc = 1** (30 жанра): най-добър модел **XGBoost + RandomizedSearch**
#   - acc = 0.2392, macro F1 = 0.2441  
#   - train = 9147, test = 2287  
#   Този супер-клас съдържа **много жанрове (30)**, което прави задачата сложна. XGBoost се справя най-добре благодарение на способността си да улавя нелинейни зависимости.
#
# - **sc = 2** (25 жанра): най-добър модел **XGBoost + RandomizedSearch**
#   - acc = 0.3662, macro F1 = 0.3430  
#   - train = 8355, test = 2089  
#   Въпреки 25-те жанра, този супер-клас показва **най-високата точност** сред по-големите групи. Вероятно жанровете тук са по-различими по аудио характеристики.
#
# - **sc = 3** (35 жанра): най-добър модел **Random Forest + RandomizedSearch**
#   - acc = 0.2468, macro F1 = 0.2496  
#   - train = 11733, test = 2933  
#   С **най-много жанрове (35)** и най-голям train set, този супер-клас е **най-труден за класификация**. Random Forest е избран заради по-добрата генерализация при много класове.
#
# - **sc = 4** (33 жанра): най-добър модел **Random Forest + RandomizedSearch**
#   - acc = 0.2839, macro F1 = 0.2573  
#   - train = 3749, test = 937  
#   Въпреки **най-малкия train set**, резултатите са сравнително добри. Ограниченият брой примери (3749) може да е причина за по-ниските метрики в сравнение с други класове.
#
# - **sc = 5** (33 жанра): най-добър модел **Random Forest + RandomizedSearch**
#   - acc = 0.2539, macro F1 = 0.2480  
#   - train = 15933, test = 3984  
#   **Най-големият train set** (15933 примера), но много жанрове (33) водят до по-ниска точност. Random Forest се справя най-добре с разнообразието от данни.
#
# - **sc = 6** (33 жанра): най-добър модел **Random Forest + RandomizedSearch**
#   - acc = 0.3912, macro F1 = 0.3587  
#   - train = 7486, test = 1871  
#   **Най-висок резултат** сред всички супер-класове. Въпреки 33-те жанра, данните в този клас изглежда са по-добре разделими, което позволява на Random Forest да постигне значително по-добри метрики.
#
# ### 3) Общ извод от втория слой
# Резултатите потвърждават, че **трудността на задачата зависи силно от броя жанрове и тяхната близост** в рамките на даден супер-клас:
# - При супер-класове с много жанрове (sc=3 с 35 жанра) точността и macro F1 са по-ниски.
# - **XGBoost** се оказва най-добър за sc=1 и sc=2, докато **Random Forest** доминира при останалите супер-класове.
# - Средна точност: **~0.30**, среден macro F1: **~0.28**
#
# ### 4) Какво означава това за двустепенната система
# Комбинацията от силен модел за супер-клас (kNN с 96% accuracy) и специализирани модели за жанр по супер-клас (XGBoost / Random Forest с RandomizedSearch) показва, че „разделяй и владей" работи като стратегия: първият слой надеждно ограничава търсенето до релевантна група, а вторият слой се оптимизира според спецификата на конкретния супер-клас.
#
# Обобщено: системата е най-надеждна при супер-класове с по-добре разделими жанрове (sc=6, sc=2), докато при супер-класове с много и близки жанрове (sc=3, sc=1) основното предизвикателство остава финото разграничаване между тях.

# %% [markdown] id="K5RnmcxdTNAq"
# # Обобщение на резултатите от проекта
#
# ### Какво направихме
# - Заредихме и почистихме dataset със Spotify аудио характеристики (таблични признаци).
# - Направихме първоначален EDA и визуализации: разпределения на признаци, дисбаланс на жанровете и базови статистики.
# - **Част 1 (класификация на жанр):** обучихме и сравнихме няколко класически модела (LogReg, kNN, SVM, Decision Tree, Random Forest, MLP) с метрики **Accuracy** и **Macro F1**.
# - **Част 2 (клъстеризация):** групирахме песни по „vibe“ на база аудио признаци и описахме клъстерите.
# - **Част 3 (super-classes):** използвахме получените vibe групи като „супер-класове“ и приложихме двустепенна (hierarchical) класификация: **superclass → genre**.
#
# ### Какви резултати постигнахме (кратко)
# - При директна **многокласова класификация на жанр** най-добро представяне има **Random Forest** (около `acc≈0.32`, `macro F1≈0.31` върху използвания поднабор/разделяне).
# - При **предсказване на супер-клас (6 vibe класа)** резултатите са значително по-високи (около `acc≈0.96`, `macro F1≈0.95`), което показва, че vibe групите са добре разделими по признаците.
# - При **втория слой (жанр вътре в супер-клас)** представянето варира според броя и близостта на жанровете в съответния супер-клас (по-високо при малък брой жанрове; по-ниско при супер-класове с много близки жанрове).
#
# ### Важни бележки за интерпретация
# - Част от експериментите са върху **извадково подмножество** (за да се вместим в ресурсите при агломеративна клъстеризация). Това влияе на дисбаланса и трудността на задачата.
# - В йерархичния подход супер-класовете са извлечени чрез **клъстеризация върху целия наличен поднабор**, което може да пренесе информация към test. За строго сравнение: клъстеризацията трябва да се обучи само върху train и после да се присвоят класове на test.
#
# ### Бъдещи разширения
# - По-стабилна оценка: **nested CV**, повече split-ове или cross-validation и отделен final holdout тест.
# - По-силни модели/признаци: gradient boosting (XGBoost/LightGBM), feature engineering, one-hot за `key/mode/time_signature`.
# - Модели върху аудио репрезентации (спектрограми, embeddings) вместо само таблични признаци.
# - По-строга йерархична схема: fit на clustering само върху train + model calibration и измерване на coverage (жанрове, видени в train).
#
