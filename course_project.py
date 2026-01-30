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

# %% [markdown] cell_id="d2072d08be074b5eac232f64efc9ced6" deepnote_app_block_group_id deepnote_app_block_order=0 deepnote_app_block_visible=true deepnote_block_group="725a1be99d2e40c798dc6da65f026532" deepnote_cell_type="text-cell-h1" deepnote_sorting_key="0" deepnote_source="\u0414\u043e\u043c\u0430\u0448\u043d\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 3" formattedRanges=[]
# # Курсова работа

# %% [markdown] cell_id="caecadd6dcbf4e8eba85cb9d25c300e4" deepnote_block_group="78894b0f566243b0b1f1dd1a00af9a58" deepnote_cell_type="markdown" deepnote_sorting_key="1" deepnote_source="## \u0415\u043a\u0438\u043f\n\n- **\u041c\u0438\u043a\u0438\u0442\u0430 \u0411\u0438\u043b\u0438\u0439** \u2013 \u0424\u0430\u043a\u0443\u043b\u0442\u0435\u0442\u0435\u043d \u043d\u043e\u043c\u0435\u0440: **9MI8000022**  \n  \u0411\u0430\u043a\u0430\u043b\u0430\u0432\u044a\u0440\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0430: **\u201e\u0421\u043e\u0444\u0442\u0443\u0435\u0440\u043d\u043e \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0441\u0442\u0432\u043e\u201c**\n\n- **\u0420\u0430\u044f \u0413\u0440\u0438\u0433\u043e\u0440\u043e\u0432\u0430** \u2013 \u0424\u0430\u043a\u0443\u043b\u0442\u0435\u0442\u0435\u043d \u043d\u043e\u043c\u0435\u0440: **5MI0600167**  \n  \u0411\u0430\u043a\u0430\u043b\u0430\u0432\u044a\u0440\u0441\u043a\u0430 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u0430: **\u201e\u0421\u043e\u0444\u0442\u0443\u0435\u0440\u043d\u043e \u0438\u043d\u0436\u0435\u043d\u0435\u0440\u0441\u0442\u0432\u043e\u201c**\n"
# ## Екип
#
# - **Микита Билий** – Факултетен номер: **9MI8000022**  
#   Бакалавърска програма: **„Софтуерно инженерство“**
#
# - **Рая Григорова** – Факултетен номер: **5MI0600167**  
#   Бакалавърска програма: **„Софтуерно инженерство“**
#

# %% [markdown] cell_id="532964dca58e4ae3b2ff53919cf7db39" deepnote_block_group="38f764e5cef64e239bc5099c14f47c72" deepnote_cell_type="markdown" deepnote_sorting_key="2" deepnote_source="## \u0422\u0438\u043f \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430\n- **C. \u0421\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u0430 \u0442\u0435\u043c\u0430** \u2013 \u043f\u0440\u043e\u0435\u043a\u0442 \u0432\u044a\u0440\u0445\u0443 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e \u0434\u043e\u0441\u0442\u044a\u043f\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (Kaggle), \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d \u0432 Python (Jupyter Notebook), \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0449 \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f.\n\n## \u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 (\u043f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442)\n- **\u201e\u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0447\u0440\u0435\u0437 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u201c**  \n  **\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u043d\u0430 \u043e\u0431\u043b\u0430\u0441\u0442:** \u041c\u0430\u0448\u0438\u043d\u043d\u043e \u0441\u0430\u043c\u043e\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u0432\u044a\u0440\u0445\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f)\n"
# ## Тип на проекта
# - **C. Собствена тема** – проект върху публично достъпни данни (Kaggle), реализиран в Python (Jupyter Notebook), включващ задачи по класификация и клъстеризация.
#
# ## Название на проекта (предметна област)
# - **„Класификация на музикални жанрове и групиране на песни по настроение чрез таблични аудио характеристики“**  
#   **Предметна област:** Машинно самообучение върху таблични данни (класификация и клъстеризация)
#

# %% [markdown] cell_id="fac6c5cbb4d447d1b7ed0f7d55451df3" deepnote_block_group="499ce469ca4c40b78030820b83a03fd1" deepnote_cell_type="markdown" deepnote_sorting_key="3" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430\n\n\u0426\u0435\u043b\u0442\u0430 \u043d\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0435 \u0434\u0430 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430 \u0434\u043e\u043a\u043e\u043b\u043a\u043e **\u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438**, \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u043e\u0442 Spotify, \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u043e \u0441\u044a\u0434\u044a\u0440\u0436\u0430\u043d\u0438\u0435 \u0447\u0440\u0435\u0437 \u043c\u0435\u0442\u043e\u0434\u0438 \u0437\u0430 \u043c\u0430\u0448\u0438\u043d\u043d\u043e \u0441\u0430\u043c\u043e\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435. \u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u043a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430 \u0434\u0432\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 \u0437\u0430\u0434\u0430\u0447\u0438: **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435** \u0438 **\u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u0435\u043d (mood) \u043f\u0440\u043e\u0444\u0438\u043b**.\n\n\u0412 \u043f\u044a\u0440\u0432\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f, \u043f\u0440\u0438 \u043a\u043e\u044f\u0442\u043e \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u0436\u0430\u043d\u0440\u044a\u0442 \u043d\u0430 \u0434\u0430\u0434\u0435\u043d\u0430 \u043f\u0435\u0441\u0435\u043d \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043a\u0430\u0442\u043e *danceability, energy, acousticness, valence* \u0438 \u0434\u0440\u0443\u0433\u0438. \u0426\u0435\u043b\u0442\u0430 \u0435 \u0434\u0430 \u0441\u0435 \u0441\u0440\u0430\u0432\u043d\u044f\u0442 \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u043a\u043e\u0438 \u043e\u0442 \u0442\u044f\u0445 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0435 \u043f\u0440\u0438 \u0442\u0430\u0437\u0438 \u0437\u0430\u0434\u0430\u0447\u0430.\n\n\u0412\u044a\u0432 \u0432\u0442\u043e\u0440\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0432\u044a\u0440\u0445\u0443 \u0441\u044a\u0449\u0438\u0442\u0435 \u0438\u043b\u0438 \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441 \u0446\u0435\u043b **\u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435**, \u0431\u0435\u0437 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u043e \u0437\u0430\u0434\u0430\u0434\u0435\u043d\u0438 \u0435\u0442\u0438\u043a\u0435\u0442\u0438. \u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0442\u0435 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438 \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0438\u0440\u0430\u043d\u0438 \u0447\u0440\u0435\u0437 \u043e\u0431\u043e\u0431\u0449\u0435\u043d\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 \u043d\u0430 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0438\u0437\u0432\u0435\u0436\u0434\u0430\u043d\u0435 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u0444\u0438\u043b\u0438 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435.\n\n\u041a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430\u043d\u0435\u0442\u043e \u043d\u0430 \u0442\u0435\u0437\u0438 \u0434\u0432\u0435 \u0437\u0430\u0434\u0430\u0447\u0438 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u043f\u043e-\u043f\u044a\u043b\u043d\u043e \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u2013 \u043a\u0430\u043a\u0442\u043e \u043e\u0442 \u0433\u043b\u0435\u0434\u043d\u0430 \u0442\u043e\u0447\u043a\u0430 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0430 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442, \u0442\u0430\u043a\u0430 \u0438 \u043f\u043e \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0435 \u043d\u0430 \u0432\u044a\u0442\u0440\u0435\u0448\u043d\u0438\u0442\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0435\u0441\u043d\u0438\u0442\u0435, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0435 \u0443\u043b\u0430\u0432\u044f\u0442 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u0442\u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u0438.\n"
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

# %% [markdown] cell_id="3b0ccfb7a06c4dbca5489b429cadbf4d" deepnote_block_group="9ab58838d7cd488288d7b407702290b2" deepnote_cell_type="markdown" deepnote_sorting_key="4" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0438\u0442\u0435 \u0434\u0430\u043d\u043d\u0438\n\n\u0412 \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e \u0434\u043e\u0441\u0442\u044a\u043f\u0435\u043d \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u043e\u0442 \u043f\u043b\u0430\u0442\u0444\u043e\u0440\u043c\u0430\u0442\u0430 Kaggle \u2013 **[Spotify Tracks Genre Dataset](https://www.kaggle.com/datasets/thedevastator/spotify-tracks-genre-dataset)** (`thedevastator/spotify-tracks-genre-dataset`), \u043a\u043e\u0439\u0442\u043e \u0435 \u0438\u0437\u0442\u0435\u0433\u043b\u0435\u043d \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u0432 \u0440\u0430\u0431\u043e\u0442\u043d\u0430\u0442\u0430 \u0441\u0440\u0435\u0434\u0430 \u0447\u0440\u0435\u0437 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430\u0442\u0430 `kagglehub`. \u041d\u0430\u0431\u043e\u0440\u044a\u0442 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u0441\u044a\u0434\u044a\u0440\u0436\u0430 \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e\u0434\u0433\u043e\u0442\u0432\u0435\u043d\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u0437\u0430 \u043f\u0435\u0441\u043d\u0438 \u043e\u0442 Spotify \u0438 \u0435 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d \u0437\u0430 \u0430\u043d\u0430\u043b\u0438\u0437 \u0438 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u043d\u0435 \u0432\u044a\u0440\u0445\u0443 \u0432\u0435\u0447\u0435 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438.\n\n\u0414\u0430\u043d\u043d\u0438\u0442\u0435 \u0441\u0430 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u0432 \u0442\u0430\u0431\u043b\u0438\u0447\u0435\u043d \u0444\u043e\u0440\u043c\u0430\u0442 (`CSV` \u0444\u0430\u0439\u043b \u2013 `train.csv`) \u0438 \u0441\u044a\u0434\u044a\u0440\u0436\u0430\u0442 \u043f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u0435\u043b\u043d\u043e **114 000 \u0437\u0430\u043f\u0438\u0441\u0430** \u0441 **20 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0430**, \u043a\u0430\u0442\u043e \u0432\u0441\u0435\u043a\u0438 \u0437\u0430\u043f\u0438\u0441 \u043e\u0442\u0433\u043e\u0432\u0430\u0440\u044f \u043d\u0430 \u0435\u0434\u043d\u0430 \u043f\u0435\u0441\u0435\u043d. \u0427\u0430\u0441\u0442 \u043e\u0442 \u043a\u043e\u043b\u043e\u043d\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0432\u0430\u0442 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0438 \u0438 \u043e\u043f\u0438\u0441\u0430\u0442\u0435\u043b\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 (\u043d\u0430\u043f\u0440. `track_id`, `artists`, `album_name`, `track_name`), \u0430 \u043e\u0441\u0442\u0430\u043d\u0430\u043b\u0438\u0442\u0435 \u2013 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u043e\u043f\u0438\u0441\u0432\u0430\u0449\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438\u0442\u0435 \u0441\u0432\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435.\n\n\u041e\u0441\u043d\u043e\u0432\u043d\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0438 \u0432 \u043f\u0440\u043e\u0435\u043a\u0442\u0430, \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0442:\n- *danceability*, *energy*, *loudness*, *speechiness*, *acousticness*,\n- *instrumentalness*, *liveness*, *valence*, *tempo*,\n\u043a\u0430\u043a\u0442\u043e \u0438 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u043a\u0430\u0442\u043e \u043f\u0440\u043e\u0434\u044a\u043b\u0436\u0438\u0442\u0435\u043b\u043d\u043e\u0441\u0442 (`duration_ms`), \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442 (`popularity`), \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u043a\u043b\u044e\u0447 \u0438 \u0442\u0430\u043a\u0442.\n\n\u0426\u0435\u043b\u0435\u0432\u0430\u0442\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0437\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043f\u043e \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0435 \u043a\u043e\u043b\u043e\u043d\u0430\u0442\u0430 **`track_genre`**, \u043a\u043e\u044f\u0442\u043e \u0441\u044a\u0434\u044a\u0440\u0436\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u044f \u0435\u0442\u0438\u043a\u0435\u0442 \u043d\u0430 \u0432\u0441\u044f\u043a\u0430 \u043f\u0435\u0441\u0435\u043d. \u0417\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043f\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u043e\u0432\u0430\u0442\u0430 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f."
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

# %% [markdown] cell_id="7715c7f0a7a44b228158e00e6ae12887" deepnote_block_group="2bdcbc20d7b04a0d8d1a8c1d06c808f7" deepnote_cell_type="markdown" deepnote_sorting_key="5" deepnote_source="## \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0438 \u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u0435\u043d EDA \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435\n\n\u0412 \u0442\u0430\u0437\u0438 \u0441\u0435\u043a\u0446\u0438\u044f \u0441\u0435 \u043f\u0440\u0430\u0432\u0438 **\u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u043d\u043e \u043e\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438** \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0434\u0430\u043b\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u043e\u0441\u044f\u0442 \u0441\u0438\u0433\u043d\u0430\u043b \u0437\u0430 \u0436\u0430\u043d\u0440\u0430 \u0438 \u0437\u0430 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u043e \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435.\n\n\u041d\u0430 \u0432\u0438\u0441\u043e\u043a\u043e \u043d\u0438\u0432\u043e \u043a\u043e\u0434\u044a\u0442:\n- \u0438\u043d\u0441\u0442\u0430\u043b\u0438\u0440\u0430 \u043d\u0443\u0436\u043d\u0438\u0442\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 (`kagglehub`, `statsmodels`) \u0438 **\u0438\u0437\u0442\u0435\u0433\u043b\u044f** \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u0430 \u043e\u0442 Kaggle;\n- **\u0437\u0430\u0440\u0435\u0436\u0434\u0430** `train.csv` \u0432 `pandas` DataFrame \u0438 \u043f\u0440\u0430\u0432\u0438 \u0431\u0430\u0437\u043e\u0432\u0430 \u0438\u043d\u0441\u043f\u0435\u043a\u0446\u0438\u044f (\u043f\u0440\u0435\u0433\u043b\u0435\u0434 \u043d\u0430 \u0440\u0435\u0434\u043e\u0432\u0435/\u043a\u043e\u043b\u043e\u043d\u0438, \u0443\u043d\u0438\u043a\u0430\u043b\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435);\n- \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0432\u0430 \u0437\u0430 **\u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438**;\n- \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u0430 **\u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f** \u043d\u0430 \u043a\u043b\u044e\u0447\u043e\u0432\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (`danceability`, `energy`, `tempo`) \u0438 \u043d\u0430 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0438 (`explicit`, `mode`, `key`);\n- \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 **\u0432\u0440\u044a\u0437\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435** \u0447\u0440\u0435\u0437 pairplot \u0438 \u043a\u043e\u0440\u0435\u043b\u0430\u0446\u0438\u043e\u043d\u043d\u0430 \u043c\u0430\u0442\u0440\u0438\u0446\u0430;\n- \u0441\u0440\u0430\u0432\u043d\u044f\u0432\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 **\u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435** (\u043d\u0430\u043f\u0440. boxplot \u043d\u0430 `energy` \u043f\u043e \u0436\u0430\u043d\u0440, \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 major/minor \u043f\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435);\n- \u043f\u0440\u0430\u0432\u0438 **PCA \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f** \u0437\u0430 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (\u0441\u043b\u0435\u0434 \u0441\u043a\u0430\u043b\u0438\u0440\u0430\u043d\u0435), \u0437\u0430 \u0434\u0430 \u0441\u0435 \u0432\u0438\u0434\u0438 \u0434\u0430\u043b\u0438 \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430 \u0435\u0441\u0442\u0435\u0441\u0442\u0432\u0435\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435;\n- \u043f\u0440\u0430\u0432\u0438 **\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430** \u043a\u043e\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u043e \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 (ANOVA + \u0435\u0444\u0435\u043a\u0442 \u0440\u0430\u0437\u043c\u0435\u0440) \u0438 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (Tukey HSD)."
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

# %% cell_id="a7c491d1294547f29ffa80cf055d0d74" deepnote_block_group="a38f6c1009874338a9c986e5827f9f72" deepnote_cell_type="code" deepnote_content_hash="20199392" deepnote_execution_finished_at="2026-01-27T21:47:00.392Z" deepnote_execution_started_at="2026-01-27T21:47:00.138Z" deepnote_sorting_key="6" deepnote_source="# \u041e\u0441\u043d\u043e\u0432\u043d\u0438 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438\nimport numpy as np\nimport pandas as pd\n\n# \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\n# \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 (EDA/\u0437\u043d\u0430\u0447\u0438\u043c\u043e\u0441\u0442)\nfrom scipy import stats\nfrom statsmodels.stats.multicomp import pairwise_tukeyhsd\n\n# Scikit-learn: preprocessing / dim reduction / split / pipeline\nfrom sklearn.compose import ColumnTransformer\nfrom sklearn.decomposition import PCA\nfrom sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV\nfrom sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler\n\n# Scikit-learn: \u043c\u043e\u0434\u0435\u043b\u0438\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.svm import LinearSVC\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.neural_network import MLPClassifier\n\n# Scikit-learn: \u043c\u0435\u0442\u0440\u0438\u043a\u0438\nfrom sklearn.metrics import (\n    accuracy_score,\n    f1_score,\n    classification_report,\n    confusion_matrix,\n    ConfusionMatrixDisplay\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=254 execution_start=1769550420138 source_hash="20199392"
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

# Scikit-learn: метрики
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# %% cell_id="9b33424659a94d278da08c3acf250d86" deepnote_app_block_group_id deepnote_app_block_order=3 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="0604134473cd4f099f9b2422fe12bf12" deepnote_cell_type="code" deepnote_content_hash="ed7bd955" deepnote_execution_finished_at="2026-01-27T21:46:48.693Z" deepnote_execution_started_at="2026-01-27T21:46:40.377Z" deepnote_sorting_key="7" deepnote_source="!pip install kagglehub statsmodels" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=8316 execution_start=1769550400377 source_hash="ed7bd955"
# !pip install kagglehub statsmodels

# %% cell_id="f38564bca7294c72ae304eb1b933c5c1" deepnote_app_block_group_id deepnote_app_block_order=4 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="da14cae1b4ce404abfc1a9afd1e53b16" deepnote_cell_type="code" deepnote_content_hash="7b09edc6" deepnote_execution_finished_at="2026-01-27T21:47:06.292Z" deepnote_execution_started_at="2026-01-27T21:47:05.171Z" deepnote_sorting_key="8" deepnote_source="import kagglehub\n\n# Download latest version\npath = kagglehub.dataset_download(\"thedevastator/spotify-tracks-genre-dataset\")\n\nprint(\"Path to dataset files:\", path)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=1121 execution_start=1769550425171 source_hash="7b09edc6"
import kagglehub

# Download latest version
path = kagglehub.dataset_download("thedevastator/spotify-tracks-genre-dataset")

print("Path to dataset files:", path)

# %% cell_id="1c371fdcf3b34d8bb2defa8edf5829be" deepnote_app_block_group_id deepnote_app_block_order=6 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="029282de92cd4f2cbc248e3ad05822ce" deepnote_cell_type="code" deepnote_content_hash="632f1b13" deepnote_execution_finished_at="2026-01-27T20:25:48.242Z" deepnote_execution_started_at="2026-01-27T20:25:48.151Z" deepnote_sorting_key="9" deepnote_source="!ls /root/.cache/kagglehub/datasets/thedevastator/spotify-tracks-genre-dataset/versions/1" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=91 execution_start=1769545548151 source_hash="632f1b13"
# !ls /root/.cache/kagglehub/datasets/thedevastator/spotify-tracks-genre-dataset/versions/1

# %% cell_id="da89c73b27d940778c52c96f6e727cab" deepnote_app_block_group_id deepnote_app_block_order=7 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b3edfdac08594ff48d21af698feb86b7" deepnote_cell_type="code" deepnote_content_hash="1f94353e" deepnote_execution_finished_at="2026-01-27T21:47:10.899Z" deepnote_execution_started_at="2026-01-27T21:47:10.524Z" deepnote_sorting_key="10" deepnote_source="df = pd.read_csv(path + '/train.csv', index_col=0)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=375 execution_start=1769550430524 source_hash="1f94353e"
df = pd.read_csv(path + '/train.csv', index_col=0)

# %% cell_id="a496a2251bc44d1a8f235dbfeed294a8" deepnote_block_group="0592c33a4e3e4179be0693a6473e37d8" deepnote_cell_type="code" deepnote_content_hash="14f60b8f" deepnote_execution_finished_at="2026-01-27T20:25:48.651Z" deepnote_execution_started_at="2026-01-27T20:25:48.651Z" deepnote_sorting_key="11" deepnote_source="df.shape" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548651 source_hash="14f60b8f"
df.shape

# %% cell_id="2fcf49e86b734a51b4609dd1cbd432a3" deepnote_app_block_group_id deepnote_app_block_order=8 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="4abaa37a99e248b399fc9d6efc215898" deepnote_cell_type="code" deepnote_content_hash="f804c160" deepnote_execution_finished_at="2026-01-27T20:25:48.701Z" deepnote_execution_started_at="2026-01-27T20:25:48.701Z" deepnote_sorting_key="12" deepnote_source="df" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548701 source_hash="f804c160"
df

# %% cell_id="65dfeb04f3b24e1cbc55b1c3be13be98" deepnote_app_block_group_id deepnote_app_block_order=9 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="ec9c7b7e4b5a4a698837d4b23d80bb74" deepnote_cell_type="code" deepnote_content_hash="f9e39fdf" deepnote_execution_finished_at="2026-01-27T20:25:48.781Z" deepnote_execution_started_at="2026-01-27T20:25:48.781Z" deepnote_sorting_key="13" deepnote_source="np.unique(df['track_genre'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545548781 source_hash="f9e39fdf"
np.unique(df['track_genre'])

# %% cell_id="8f67056ec7a14c3080ad94b5840a7e19" deepnote_app_block_group_id deepnote_app_block_order=10 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="be1370a7815448cab2deb7669c1a5987" deepnote_cell_type="code" deepnote_content_hash="eeb3f9d8" deepnote_execution_finished_at="2026-01-27T20:25:49.704Z" deepnote_execution_started_at="2026-01-27T20:25:48.831Z" deepnote_sorting_key="14" deepnote_source="# Set a larger figure size so the list fits\nplt.figure(figsize=(12, 20)) \n\nplt.title(\"Distribution of tracks per genres\")\n# Swap x and y (put genre on Y-axis)\nsns.countplot(y='track_genre', data=df) \n# OR if using barplot: sns.barplot(x='popularity', y='track_genre', data=df)\n\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=873 execution_start=1769545548831 source_hash="eeb3f9d8"
# Set a larger figure size so the list fits
plt.figure(figsize=(12, 20)) 

plt.title("Distribution of tracks per genres")
# Swap x and y (put genre on Y-axis)
sns.countplot(y='track_genre', data=df) 
# OR if using barplot: sns.barplot(x='popularity', y='track_genre', data=df)

plt.show()

# %% cell_id="100e5efccba444c9857c026d2754fa15" deepnote_app_block_group_id deepnote_app_block_order=11 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="3d650264fd324687bc541b052b910e02" deepnote_cell_type="code" deepnote_content_hash="dbc998a9" deepnote_execution_finished_at="2026-01-27T20:25:49.996Z" deepnote_execution_started_at="2026-01-27T20:25:49.761Z" deepnote_sorting_key="15" deepnote_source="plt.figure(figsize=(20, 5))\nsns.boxplot(data=df, x='duration_ms')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=235 execution_start=1769545549761 source_hash="dbc998a9"
plt.figure(figsize=(20, 5))
sns.boxplot(data=df, x='duration_ms')
plt.show()

# %% cell_id="0d9cd2d9adb447209bc9c4cf82f5a232" deepnote_app_block_group_id deepnote_app_block_order=12 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="64146747b61549a0a3a5e52769883a3d" deepnote_cell_type="code" deepnote_content_hash="4d04b885" deepnote_execution_finished_at="2026-01-27T20:25:50.041Z" deepnote_execution_started_at="2026-01-27T20:25:50.041Z" deepnote_sorting_key="16" deepnote_source="if df.isnull().values.any():\n    print(\"Missing values found!\")\n    print(\"-\" * 30)\n    # Show count of NaNs per column\n    print(df.isnull().sum())\nelse:\n    print(\"No missing values found in the DataFrame.\")" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545550041 source_hash="4d04b885"
if df.isnull().values.any():
    print("Missing values found!")
    print("-" * 30)
    # Show count of NaNs per column
    print(df.isnull().sum())
else:
    print("No missing values found in the DataFrame.")

# %% cell_id="2ec38365549f4eef8a21af3fb2352848" deepnote_app_block_group_id deepnote_app_block_order=13 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="77b188c1d223447d9906ab113414ef18" deepnote_cell_type="code" deepnote_content_hash="25d43fa0" deepnote_execution_finished_at="2026-01-27T20:25:50.101Z" deepnote_execution_started_at="2026-01-27T20:25:50.101Z" deepnote_sorting_key="17" deepnote_source="df.columns" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545550101 source_hash="25d43fa0"
df.columns

# %% cell_id="5e3011cf86514a05a3f45ebf5c88eda7" deepnote_app_block_group_id deepnote_app_block_order=14 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="00a945ab35094ba694655233f74bd163" deepnote_cell_type="code" deepnote_content_hash="7f1878dd" deepnote_execution_finished_at="2026-01-27T20:25:50.861Z" deepnote_execution_started_at="2026-01-27T20:25:50.161Z" deepnote_sorting_key="18" deepnote_source="sns.histplot(x=df['danceability'], kde=True, bins='auto')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=700 execution_start=1769545550161 source_hash="7f1878dd"
sns.histplot(x=df['danceability'], kde=True, bins='auto')
plt.show()

# %% cell_id="949758369c1c4ddf89b1dcb08226f991" deepnote_app_block_group_id deepnote_app_block_order=15 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="f7a005f68b454716bdd2d8b4e2f44f39" deepnote_cell_type="code" deepnote_content_hash="15a58f46" deepnote_execution_finished_at="2026-01-27T20:25:51.491Z" deepnote_execution_started_at="2026-01-27T20:25:50.911Z" deepnote_sorting_key="19" deepnote_source="sns.histplot(x=df['energy'], kde=True, bins='auto')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=580 execution_start=1769545550911 source_hash="15a58f46"
sns.histplot(x=df['energy'], kde=True, bins='auto')
plt.show()

# %% cell_id="5018ecddc6b143a7a97df2ed4a438196" deepnote_app_block_group_id deepnote_app_block_order=16 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="4fb74fcd6951406cb3afafac01cbd2bc" deepnote_cell_type="code" deepnote_content_hash="eb8966df" deepnote_execution_finished_at="2026-01-27T20:25:51.541Z" deepnote_execution_started_at="2026-01-27T20:25:51.541Z" deepnote_sorting_key="20" deepnote_source="df['explicit'].value_counts().plot(kind='bar', color=['red', 'green'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545551541 source_hash="eb8966df"
df['explicit'].value_counts().plot(kind='bar', color=['red', 'green'])

# %% cell_id="80a90f261f4441e1a9f643277b7c33ab" deepnote_app_block_group_id deepnote_app_block_order=17 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1d46b2b139b649b497527c3dfff9f02b" deepnote_cell_type="code" deepnote_content_hash="11a9c500" deepnote_execution_finished_at="2026-01-27T20:25:51.718Z" deepnote_execution_started_at="2026-01-27T20:25:51.661Z" deepnote_sorting_key="21" deepnote_source="df['mode'].value_counts().plot(kind='bar')\nplt.xticks(ticks=[0, 1], labels=['minor', 'major'])\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=57 execution_start=1769545551661 source_hash="11a9c500"
df['mode'].value_counts().plot(kind='bar')
plt.xticks(ticks=[0, 1], labels=['minor', 'major'])
plt.show()

# %% cell_id="21184c4631df4fc38c840e17f921c1d0" deepnote_app_block_group_id deepnote_app_block_order=18 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1413a34a3aea4904aa20b9a8466918bf" deepnote_cell_type="code" deepnote_content_hash="c33227cf" deepnote_execution_finished_at="2026-01-27T20:25:51.771Z" deepnote_execution_started_at="2026-01-27T20:25:51.771Z" deepnote_sorting_key="22" deepnote_source="np.unique(df['key'])" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545551771 source_hash="c33227cf"
np.unique(df['key'])

# %% cell_id="60fababd386a4cfab2ec0fc6d039af74" deepnote_app_block_group_id deepnote_app_block_order=19 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="febfd683232c489b961ee9884a9e7219" deepnote_cell_type="code" deepnote_content_hash="81f6827a" deepnote_execution_finished_at="2026-01-27T20:25:51.892Z" deepnote_execution_started_at="2026-01-27T20:25:51.821Z" deepnote_sorting_key="23" deepnote_source="key_map = {\n    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', \n    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'\n}\n\ndf['key_name'] = df['key'].map(key_map)\n\ndf['key_name'].value_counts().sort_index().plot(kind='bar')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=71 execution_start=1769545551821 source_hash="81f6827a"
key_map = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

df['key_name'] = df['key'].map(key_map)

df['key_name'].value_counts().sort_index().plot(kind='bar')
plt.show()

# %% cell_id="ce698f31a3f64f20a880b9c6d34b5a93" deepnote_app_block_group_id deepnote_app_block_order=20 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="5157d4f03b5d44b9874933a6a81b319c" deepnote_cell_type="code" deepnote_content_hash="8ccda497" deepnote_execution_finished_at="2026-01-27T20:25:52.682Z" deepnote_execution_started_at="2026-01-27T20:25:52.131Z" deepnote_sorting_key="24" deepnote_source="sns.histplot(x=df['tempo'], kde=True)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=551 execution_start=1769545552131 source_hash="8ccda497"
sns.histplot(x=df['tempo'], kde=True)

# %% cell_id="69207c260f7545398eaa727b003609a9" deepnote_app_block_group_id deepnote_app_block_order=21 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="620b1255fc5041f19d7fd52dafc2c6f1" deepnote_cell_type="code" deepnote_content_hash="48fb3ce1" deepnote_execution_finished_at="2026-01-27T20:25:52.813Z" deepnote_execution_started_at="2026-01-27T20:25:52.711Z" deepnote_sorting_key="25" deepnote_source="key_mode_pivot = pd.crosstab(df['key'], df['mode'])\n\nkey_mode_pivot.index = key_map.values()\nkey_mode_pivot.columns = ['Minor', 'Major']\n\nsns.heatmap(key_mode_pivot, annot=True, fmt='d', cmap='YlGnBu')\nplt.title('Frequency of Musical Keys by Mode')" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=102 execution_start=1769545552711 source_hash="48fb3ce1"
key_mode_pivot = pd.crosstab(df['key'], df['mode'])

key_mode_pivot.index = key_map.values()
key_mode_pivot.columns = ['Minor', 'Major']

sns.heatmap(key_mode_pivot, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Frequency of Musical Keys by Mode')

# %% cell_id="2350c398aa094d8186b339b34ba18530" deepnote_app_block_group_id deepnote_app_block_order=22 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="ba12533b624c466e82febaabb84c820f" deepnote_cell_type="code" deepnote_content_hash="ff9e70a4" deepnote_execution_finished_at="2026-01-27T20:25:53.729Z" deepnote_execution_started_at="2026-01-27T20:25:53.041Z" deepnote_sorting_key="26" deepnote_source="mode_dist = pd.crosstab(df['track_genre'], df['mode'], normalize='index')\nmode_dist.columns = ['Minor', 'Major']\nmode_dist = mode_dist.sort_values('Major', ascending=False)\nmode_dist.plot(kind='barh', stacked=True, figsize=(10, 25), color=['#e74c3c', '#3498db'])\n\nplt.title('Distribution (Part) of Major vs Minor Mode per Genre')\nplt.xlabel('Proportion (0.0 to 1.0)')\nplt.ylabel('Genre')\nplt.legend(title='Musical Mode', bbox_to_anchor=(1.05, 1), loc='upper left')\nplt.axvline(x=0.5, color='white', linestyle='--', alpha=0.5) # Center line for balance\nplt.tight_layout()\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=688 execution_start=1769545553041 source_hash="ff9e70a4"
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

# %% cell_id="501402681fc74736bc9cd5c63e6fec10" deepnote_app_block_group_id deepnote_app_block_order=23 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="1e56b7cbccbb44a98dfa0740a6527bed" deepnote_cell_type="code" deepnote_content_hash="625f22c7" deepnote_execution_finished_at="2026-01-27T20:25:53.781Z" deepnote_execution_started_at="2026-01-27T20:25:53.781Z" deepnote_sorting_key="27" deepnote_source="numerical_cols = ['danceability', 'energy', 'loudness', 'speechiness', \n                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545553781 source_hash="625f22c7"
numerical_cols = ['danceability', 'energy', 'loudness', 'speechiness', 
                  'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']

# %% cell_id="84e5a868e3d54777856c695d9c91ea49" deepnote_app_block_group_id deepnote_app_block_order=24 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="610f0f27d01e4e388f1fe4e7b7ac67de" deepnote_cell_type="code" deepnote_content_hash="47642bda" deepnote_execution_finished_at="2026-01-27T20:26:16.694Z" deepnote_execution_started_at="2026-01-27T20:25:53.831Z" deepnote_sorting_key="28" deepnote_source="sns.pairplot(df[numerical_cols], plot_kws={'alpha': 0.1, 's': 5}, diag_kind='kde')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=22863 execution_start=1769545553831 source_hash="47642bda"
sns.pairplot(df[numerical_cols], plot_kws={'alpha': 0.1, 's': 5}, diag_kind='kde')
plt.show()

# %% cell_id="9969ccca90c04e9b85507ab93805fbaf" deepnote_app_block_group_id deepnote_app_block_order=25 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="2868c2bbe7f54eb9a9a3369a19f42b6a" deepnote_cell_type="code" deepnote_content_hash="920d6848" deepnote_execution_finished_at="2026-01-27T20:26:17.760Z" deepnote_execution_started_at="2026-01-27T20:26:16.700Z" deepnote_sorting_key="29" deepnote_source="plt.figure(figsize=(40, 15))\nsns.boxplot(x='track_genre', y='energy', data=df)\nplt.title('Strong Signal: Energy Distribution by Genre')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1060 execution_start=1769545576700 source_hash="920d6848"
plt.figure(figsize=(40, 15))
sns.boxplot(x='track_genre', y='energy', data=df)
plt.title('Strong Signal: Energy Distribution by Genre')
plt.show()

# %% cell_id="daa3f793ae2a42c2baf102b2245a25e9" deepnote_app_block_group_id deepnote_app_block_order=26 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="671993eca58649c9810dccc9e3728eeb" deepnote_cell_type="code" deepnote_content_hash="80d00cd3" deepnote_execution_finished_at="2026-01-27T20:26:18.064Z" deepnote_execution_started_at="2026-01-27T20:26:17.821Z" deepnote_sorting_key="30" deepnote_source="plt.figure(figsize=(10, 8))\ncorr = df[numerical_cols].corr()\nsns.heatmap(corr, annot=True, fmt=\".2f\", cmap='coolwarm')\nplt.title('Feature Correlation Heatmap')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=243 execution_start=1769545577821 source_hash="80d00cd3"
plt.figure(figsize=(10, 8))
corr = df[numerical_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# %% cell_id="58bfd240f9144ba4a02a29fd30186f2e" deepnote_app_block_group_id deepnote_app_block_order=27 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="548efb1cb7134596b067c3a4b3ded594" deepnote_cell_type="code" deepnote_content_hash="38d71b6a" deepnote_execution_finished_at="2026-01-27T20:26:18.447Z" deepnote_execution_started_at="2026-01-27T20:26:18.121Z" deepnote_sorting_key="31" deepnote_source="df_vis = df.loc[(df['track_genre'] == 'black-metal') | (df['track_genre'] == 'indian') | (df['track_genre'] == 'sleep'), numerical_cols + ['track_genre']]\n\nscaler = StandardScaler()\nscaled_features = scaler.fit_transform(df_vis[numerical_cols])\n\npca = PCA(n_components=2)\npca_result = pca.fit_transform(scaled_features)\n\nplt.figure(figsize=(10, 7))\nsns.scatterplot(x=pca_result[:, 0], y=pca_result[:, 1], hue=df_vis['track_genre'], palette='viridis')\nplt.title('PCA Projection: Do the genres separate naturally?')\nplt.xlabel('Principal Component 1')\nplt.ylabel('Principal Component 2')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=326 execution_start=1769545578121 source_hash="38d71b6a"
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

# %% cell_id="e98810a7b7744a1d832e5fc84b25f76c" deepnote_app_block_group_id deepnote_app_block_order=28 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b0e81cbe825944b4a48e7f4721c1d7d5" deepnote_cell_type="code" deepnote_content_hash="26b75ea6" deepnote_execution_finished_at="2026-01-27T20:26:18.806Z" deepnote_execution_started_at="2026-01-27T20:26:18.501Z" deepnote_sorting_key="32" deepnote_source="target_genres = ['rock', 'classical', 'indian']\nsubset = df[df['track_genre'].isin(target_genres)].copy()\n\nscaler = MinMaxScaler()\nsubset[numerical_cols] = scaler.fit_transform(subset[numerical_cols])\n\nmeans = subset.groupby('track_genre')[numerical_cols].mean().reset_index()\n\nN = len(numerical_cols)\nangles = [n / float(N) * 2 * np.pi for n in range(N)]\nangles += angles[:1] # Close the loop\n\nfig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))\n\nfor index, row in means.iterrows():\n    values = row[numerical_cols].tolist()\n    values += values[:1]\n    ax.plot(angles, values, linewidth=1, linestyle='solid', label=row['track_genre'])\n    ax.fill(angles, values, alpha=0.1)\n\nplt.xticks(angles[:-1], numerical_cols)\nplt.title('Audio Feature Profile: Rock vs Classical vs Indian')\nplt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=305 execution_start=1769545578501 source_hash="26b75ea6"
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

# %% [markdown] cell_id="dfa413c245ba453e80bebeba07bc12fa" deepnote_app_block_group_id deepnote_app_block_order=29 deepnote_app_block_visible=true deepnote_block_group="46b4f4ae204b470d946f165187116194" deepnote_cell_type="text-cell-p" deepnote_sorting_key="33" deepnote_source="Somehow indian music is close to rock xD" formattedRanges=[]
# Somehow indian music is close to rock xD

# %% cell_id="c1014e9422f74f9aaa0e996f9102c997" deepnote_app_block_group_id deepnote_app_block_order=30 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="619cfc5737654e17ae282caecaf2caf4" deepnote_cell_type="code" deepnote_content_hash="63087d59" deepnote_execution_finished_at="2026-01-27T20:26:32.460Z" deepnote_execution_started_at="2026-01-27T20:26:18.871Z" deepnote_sorting_key="34" deepnote_source="results = []\n\nprint(\"--- Calculating Signal Strength (Effect Size) ---\")\n\nfor feature in numerical_cols:\n    groups = [df[df['track_genre'] == g][feature].values for g in df['track_genre'].unique()]\n    \n    # Run One-Way ANOVA\n    f_stat, p_val = stats.f_oneway(*groups)\n    \n    # Calculate Eta-Squared (Effect Size)\n    # SS_between = sum(n_i * (mean_i - grand_mean)^2)\n    # SS_total = sum((x - grand_mean)^2)\n    \n    grand_mean = df[feature].mean()\n    ss_total = np.sum((df[feature] - grand_mean)**2)\n    \n    ss_between = 0\n    for g in df['track_genre'].unique():\n        group_data = df[df['track_genre'] == g][feature]\n        n_i = len(group_data)\n        mean_i = group_data.mean()\n        ss_between += n_i * (mean_i - grand_mean)**2\n        \n    eta_squared = ss_between / ss_total\n    \n    results.append({\n        'Feature': feature,\n        'F-Statistic': f_stat,\n        'P-Value': p_val,\n        'Signal Strength (Eta^2)': eta_squared,\n        'is_significant': \"Significant Difference\" if p_val < 0.05 else \"Same Distribution\"\n    })\n\nstats_df = pd.DataFrame(results).sort_values(by='Signal Strength (Eta^2)', ascending=False)\n\nprint(stats_df[['Feature', 'Signal Strength (Eta^2)', 'P-Value', 'is_significant']].to_string(index=False))\n\nplt.figure(figsize=(10, 5))\nsns.barplot(x='Signal Strength (Eta^2)', y='Feature', data=stats_df, hue='Feature', legend=False)\nplt.title('Which Features Separate Genres Best? (Based on ANOVA Effect Size)')\nplt.xlabel('Eta-Squared (0 = No Signal, 1 = Perfect Separation)')\nplt.axvline(x=0.14, color='red', linestyle='--', label='Strong Effect Threshold (0.14)')\nplt.legend()\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=13589 execution_start=1769545578871 source_hash="63087d59"
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

# %% cell_id="10ac9e61eb1e47a8ac054ce70ae8e6a6" deepnote_app_block_group_id deepnote_app_block_order=31 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="b919ef63cfbb455c91c77f4020f71320" deepnote_cell_type="code" deepnote_content_hash="8ea4c955" deepnote_execution_finished_at="2026-01-27T20:26:32.997Z" deepnote_execution_started_at="2026-01-27T20:26:32.531Z" deepnote_sorting_key="35" deepnote_source="top_feature = stats_df.iloc[0]['Feature']\n\nprint(f\"\\n--- Running Tukey's HSD for the Top Signal: {top_feature} ---\")\n\ngenres_for_test = ['classical', 'rock', 'black-metal', 'indian', 'sleep']\ndf_test = df[df['track_genre'].isin(genres_for_test)]\n\ntukey = pairwise_tukeyhsd(endog=df_test[top_feature],\n                          groups=df_test['track_genre'],\n                          alpha=0.05)\n\nprint(tukey.summary())\n\nfig = tukey.plot_simultaneous(figsize=(12, 6))\nplt.title(f'Tukey HSD: Comparing Mean {top_feature.capitalize()}')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=466 execution_start=1769545592531 source_hash="8ea4c955"
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

# %% cell_id="00459cadaa0f4dbb94bf6bf1ae3e211d" deepnote_app_block_group_id deepnote_app_block_order=32 deepnote_app_block_visible=true deepnote_app_is_code_hidden=true deepnote_app_is_output_hidden=false deepnote_block_group="a8cbeb987f9c446da87bf50229760514" deepnote_cell_type="code" deepnote_content_hash="886180a2" deepnote_execution_finished_at="2026-01-27T20:26:33.408Z" deepnote_execution_started_at="2026-01-27T20:26:33.051Z" deepnote_sorting_key="36" deepnote_source="top_feature2 = stats_df.iloc[1]['Feature']\nprint(f\"\\n--- Running Tukey's HSD for the Top Signal: {top_feature2} ---\")\ntukey2 = pairwise_tukeyhsd(endog=df_test[top_feature2],      \n                          groups=df_test['track_genre'],   \n                          alpha=0.05)                 \n\nprint(tukey2.summary())\n\nfig = tukey2.plot_simultaneous(figsize=(12, 6))\nplt.title(f'Tukey HSD: Comparing Mean {top_feature2.capitalize()}')\nplt.show()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=357 execution_start=1769545593051 source_hash="886180a2"
top_feature2 = stats_df.iloc[1]['Feature']
print(f"\n--- Running Tukey's HSD for the Top Signal: {top_feature2} ---")
tukey2 = pairwise_tukeyhsd(endog=df_test[top_feature2],      
                          groups=df_test['track_genre'],   
                          alpha=0.05)                 

print(tukey2.summary())

fig = tukey2.plot_simultaneous(figsize=(12, 6))
plt.title(f'Tukey HSD: Comparing Mean {top_feature2.capitalize()}')
plt.show()

# %% cell_id="6517d383bd034961b8f40ca61d0203b3" deepnote_app_is_output_hidden=true deepnote_block_group="3df79550cb594508bcca1cabee30fe3b" deepnote_cell_type="code" deepnote_content_hash="5bab03ff" deepnote_execution_finished_at="2026-01-27T20:26:35.360Z" deepnote_execution_started_at="2026-01-27T20:26:33.481Z" deepnote_sorting_key="37" deepnote_source="tukey = pairwise_tukeyhsd(endog=df[top_feature],\n                          groups=df['track_genre'],\n                          alpha=0.05)\nprint(tukey.summary())" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1879 execution_start=1769545593481 is_output_hidden=true source_hash="5bab03ff"
tukey = pairwise_tukeyhsd(endog=df[top_feature],
                          groups=df['track_genre'],
                          alpha=0.05)
print(tukey.summary())

# %% cell_id="1ee43146192c4c428a4647819cf04caf" deepnote_app_is_output_hidden=true deepnote_block_group="2d339402389341399799420c21d6214e" deepnote_cell_type="code" deepnote_content_hash="67a0b53d" deepnote_execution_finished_at="2026-01-27T20:26:37.081Z" deepnote_execution_started_at="2026-01-27T20:26:35.451Z" deepnote_sorting_key="38" deepnote_source="tukey2 = pairwise_tukeyhsd(endog=df[top_feature2],      \n                          groups=df['track_genre'],   \n                          alpha=0.05)                 \n\nprint(tukey2.summary())" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1630 execution_start=1769545595451 is_output_hidden=true source_hash="67a0b53d"
tukey2 = pairwise_tukeyhsd(endog=df[top_feature2],      
                          groups=df['track_genre'],   
                          alpha=0.05)                 

print(tukey2.summary())

# %% [markdown] cell_id="dd6cb2d040f04211960c0bc802b6fa30" deepnote_block_group="333a908a48ac44daa8669455b398a2f7" deepnote_cell_type="markdown" deepnote_sorting_key="39" deepnote_source="## \u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438\u0442\u0435 \u0438 \u043f\u044a\u0440\u0432\u043e\u043d\u0430\u0447\u0430\u043b\u043d\u0438\u044f EDA\n\n- **\u0420\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435 (\u0436\u0430\u043d\u0440\u043e\u0432\u0435):** \u0413\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 \u043d\u0430 \u0431\u0440\u043e\u044f \u043f\u0435\u0441\u043d\u0438 \u043f\u043e track_genre \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0432 \u043d\u0430\u0431\u043e\u0440\u0430 \u0441\u0430 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0435\u043d\u0438 \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u043e (\u0432\u0441\u0438\u0447\u043a\u0438 \u0438\u043c\u0430\u0442 \u0440\u0430\u0432\u0435\u043d \u0431\u0440\u043e\u0439 \u0442\u0440\u0430\u043a\u043e\u0432\u0435). \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f, \u0437\u0430\u0449\u043e\u0442\u043e \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0440\u0438\u0441\u043a\u0430 \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0434\u0430 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0432\u0438\u0441\u043e\u043a\u0430 \u0442\u043e\u0447\u043d\u043e\u0441\u0442 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u043e \u0447\u0440\u0435\u0437 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043d\u0430\u0439-\u0447\u0435\u0441\u0442\u043e \u0441\u0440\u0435\u0449\u0430\u043d\u0438\u044f \u043a\u043b\u0430\u0441.\n\n- **\u041b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438:** \u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0437\u0430 NaN \u043f\u043e\u043a\u0430\u0437\u0432\u0430 **\u043c\u0438\u043d\u0438\u043c\u0430\u043b\u043d\u0438 \u043b\u0438\u043f\u0441\u0438** \u2013 \u043f\u043e 1 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0430 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442 \u0432 `artists`, `album_name` \u0438 `track_name`, \u0430 \u0432\u0441\u0438\u0447\u043a\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u0430 \u043f\u043e\u043f\u044a\u043b\u043d\u0435\u043d\u0438. \u0422\u043e\u0432\u0430 \u043e\u0437\u043d\u0430\u0447\u0430\u0432\u0430, \u0447\u0435 \u043f\u043e\u0447\u0438\u0441\u0442\u0432\u0430\u043d\u0435\u0442\u043e \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0449\u0435 \u0431\u044a\u0434\u0435 \u043b\u0435\u0441\u043d\u043e \u0438 \u043d\u044f\u043c\u0430 \u0434\u0430 \u0438\u0437\u0438\u0441\u043a\u0432\u0430 \u0441\u043b\u043e\u0436\u043d\u0438 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u0437\u0430 \u043f\u043e\u043f\u044a\u043b\u0432\u0430\u043d\u0435 \u043d\u0430 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438.\n\n- **\u0420\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438:** \u0425\u0438\u0441\u0442\u043e\u0433\u0440\u0430\u043c\u0438\u0442\u0435 \u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438\u043c\u0430\u0442 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f:\n  - \u043d\u044f\u043a\u043e\u0438 \u0441\u0430 \u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d **0\u20131** (`danceability`, `energy`, `acousticness`, `valence` \u0438 \u0434\u0440.), \u043d\u043e \u043d\u0435 \u0441\u0430 \u0440\u0430\u0432\u043d\u043e\u043c\u0435\u0440\u043d\u0438 (\u0438\u043c\u0430 \u0441\u0442\u0440\u0443\u043f\u0432\u0430\u043d\u0435 \u0432 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u043e\u0431\u043b\u0430\u0441\u0442\u0438);\n  - tempo \u043e\u0431\u0445\u0432\u0430\u0449\u0430 \u0448\u0438\u0440\u043e\u043a \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043e\u0442 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438, \u043a\u0430\u0442\u043e \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430 \u043a\u043e\u043d\u0446\u0435\u043d\u0442\u0440\u0430\u0446\u0438\u044f \u043e\u043a\u043e\u043b\u043e \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u043d\u0438 \u0442\u0435\u043c\u043f\u0430;\n  - \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 \u043d\u0430 `duration_ms` \u043f\u043e\u043a\u0430\u0437\u0432\u0430 \u0430\u0441\u0438\u043c\u0435\u0442\u0440\u0438\u0447\u043d\u043e \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0441 \u043a\u0440\u0430\u0439\u043d\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438, \u0442.\u0435. \u0438\u043c\u0430 \u0438 \u043d\u0435\u043e\u0431\u0438\u0447\u0430\u0439\u043d\u043e \u0434\u044a\u043b\u0433\u0438 \u0437\u0430\u043f\u0438\u0441\u0438, \u043a\u043e\u0435\u0442\u043e \u0435 \u043d\u043e\u0440\u043c\u0430\u043b\u043d\u043e \u0437\u0430 \u0440\u0435\u0430\u043b\u043d\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0434\u0430\u043d\u043d\u0438.\n\n- **\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0430\u043b\u043d\u0438 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0438:** `explicit` \u0435 \u0434\u0438\u0441\u0431\u0430\u043b\u0430\u043d\u0441\u0438\u0440\u0430\u043d\u0430 (\u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u043f\u0435\u0441\u043d\u0438 \u0441\u0430 False), \u0434\u043e\u043a\u0430\u0442\u043e `mode` (major/minor) \u043f\u043e\u043a\u0430\u0437\u0432\u0430 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043f\u0440\u0438 \u0440\u0430\u0437\u0431\u0438\u0432\u043a\u0430 \u043f\u043e \u0436\u0430\u043d\u0440.\n\n- **\u201eKey\u201c \u0438 \u201eMode\u201c \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442:** \u0421\u043b\u0435\u0434 \u043c\u0430\u043f\u0432\u0430\u043d\u0435\u0442\u043e \u043d\u0430 `key` \u043a\u044a\u043c \u0438\u043c\u0435\u043d\u0430 (C, C#, D, \u2026) \u0438 crosstab/heatmap \u0441\u0435 \u0432\u0438\u0436\u0434\u0430, \u0447\u0435 \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438 \u0442\u043e\u043d\u0430\u043b\u043d\u043e\u0441\u0442\u0438 \u0441\u0435 \u0441\u0440\u0435\u0449\u0430\u0442 \u043f\u043e-\u0447\u0435\u0441\u0442\u043e, \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u043d\u0435\u0442\u043e \u043d\u0430 `key` \u0437\u0430\u0435\u0434\u043d\u043e \u0441 `mode` \u0434\u0430\u0432\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442. \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u043a\u0430\u0442\u043e \u043e\u0441\u043e\u0431\u0435\u043d\u043e\u0441\u0442, \u043d\u043e \u043d\u044f\u043c\u0430 \u0434\u0430 \u0435 \u0435\u0434\u0438\u043d\u0441\u0442\u0432\u0435\u043d\u0438\u044f\u0442 \u0441\u0438\u043b\u0435\u043d \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u0442\u0435\u043b \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435.\n\n- **\u0412\u0440\u044a\u0437\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 (\u043a\u043e\u0440\u0435\u043b\u0430\u0446\u0438\u0438):** Correlation heatmap-\u044a\u0442 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438:\n  - `energy` \u0438 `loudness` \u0441\u0430 \u0441\u0438\u043b\u043d\u043e \u0441\u0432\u044a\u0440\u0437\u0430\u043d\u0438 (\u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u0441 \u043f\u043e-\u0432\u0438\u0441\u043e\u043a\u0430 \u0435\u043d\u0435\u0440\u0433\u0438\u044f \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0438\u043c\u0430\u0442 \u0438 \u043f\u043e-\u0432\u0438\u0441\u043e\u043a\u0430 \u0441\u0438\u043b\u0430 \u043d\u0430 \u0437\u0432\u0443\u043a\u0430);\n  - `acousticness` \u0435 \u0432 \u043f\u0440\u043e\u0442\u0438\u0432\u043e\u043f\u043e\u043b\u043e\u0436\u043d\u0430 \u043f\u043e\u0441\u043e\u043a\u0430 \u0441\u043f\u0440\u044f\u043c\u043e `energy`/`loudness` (\u043f\u043e-\u0430\u043a\u0443\u0441\u0442\u0438\u0447\u043d\u0438\u0442\u0435 \u043f\u0435\u0441\u043d\u0438 \u0441\u0430 \u043f\u043e-\u0442\u0438\u0445\u0438 \u0438 \u043f\u043e-\u043c\u0430\u043b\u043a\u043e \u201e\u0438\u043d\u0442\u0435\u043d\u0437\u0438\u0432\u043d\u0438\u201c);\n  - \u0438\u043c\u0430 \u0438 \u043f\u043e-\u0441\u043b\u0430\u0431\u0438/\u0443\u043c\u0435\u0440\u0435\u043d\u0438 \u0432\u0440\u044a\u0437\u043a\u0438, (\u043d\u0430\u043f\u0440. \u043c\u0435\u0436\u0434\u0443 `danceability` \u0438 `valence`) \u043a\u043e\u0438\u0442\u043e \u0441\u0430 \u0438\u043d\u0442\u0443\u0438\u0442\u0438\u0432\u043d\u043e \u043e\u0431\u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438, \u043d\u043e \u043d\u0435 \u0441\u0438\u043b\u043d\u043e \u0438\u0437\u0440\u0430\u0437\u0435\u043d\u0438.\n\n- **\u0420\u0430\u0437\u043b\u0438\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435:** Boxplot-\u0438\u0442\u0435 \u043f\u043e \u0436\u0430\u043d\u0440 (\u043d\u0430\u043f\u0440. \u0437\u0430 `energy`) \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0438\u043c\u0430\u0442 **\u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0438**, \u043d\u043e \u0441\u044a\u0449\u043e \u0438 **\u0441\u0435\u0440\u0438\u043e\u0437\u043d\u043e \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0435**. \u0422\u043e\u0432\u0430 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u044a\u0442 \u0442\u0440\u0443\u0434\u043d\u043e \u0449\u0435 \u0441\u0435 \u043e\u0442\u0434\u0435\u043b\u0438 \u0441 \u0435\u0434\u0438\u043d \u043f\u0440\u0438\u0437\u043d\u0430\u043a, \u0430 \u0449\u0435 \u0435 \u043d\u0443\u0436\u043d\u0430 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f \u043e\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449 \u043c\u043e\u0434\u0435\u043b.\n\n- **PCA \u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u0430 \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u043e\u0441\u0442:** PCA \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f\u0442\u0430 (\u0441\u043b\u0435\u0434 `StandardScaler`) \u0437\u0430 \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0438\u043c\u0430 **\u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435**, \u043d\u043e \u043d\u0435 \u0438 \u0438\u0434\u0435\u0430\u043b\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u2014 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e \u043f\u0440\u0438 \u0431\u043b\u0438\u0437\u043a\u0438 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u043d\u0438 \u0441\u0442\u0438\u043b\u043e\u0432\u0435. \u0422\u043e\u0432\u0430 \u0435 \u0434\u043e\u0431\u044a\u0440 \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440, \u0447\u0435 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0438\u043c\u0430\u0442 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430, \u043d\u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u043d\u0435 \u0435 \u0442\u0440\u0438\u0432\u0438\u0430\u043b\u043d\u0430.\n\n- **\u041f\u0440\u043e\u0444\u0438\u043b\u0438 \u043f\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0438 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f:** Radar \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0442\u0430 (\u0441\u043b\u0435\u0434 `MinMaxScaler`) \u0437\u0430 \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u0438\u0437\u0431\u0440\u0430\u043d\u0438 \u0436\u0430\u043d\u0440\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0438\u0440\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u0447\u0440\u0435\u0437 \u0441\u044a\u0432\u043a\u0443\u043f\u043d\u043e\u0441\u0442 \u043e\u0442 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438, \u0430 \u043d\u0435 \u0447\u0440\u0435\u0437 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u0430 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0430. \u0422\u043e\u0432\u0430 \u0435 \u043f\u043e\u043b\u0435\u0437\u043d\u043e \u043a\u0430\u0442\u043e \u043e\u0441\u043d\u043e\u0432\u0430 \u0438 \u0437\u0430 \u0431\u044a\u0434\u0435\u0449\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435.\n\n- **\u041a\u043e\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043d\u043e\u0441\u044f\u0442 \u043d\u0430\u0439-\u0441\u0438\u043b\u0435\u043d \u0441\u0438\u0433\u043d\u0430\u043b:** \u0415\u0444\u0435\u043a\u0442\u043d\u0438\u044f\u0442 \u0440\u0430\u0437\u043c\u0435\u0440 (eta-squared) \u0434\u0430\u0432\u0430 \u043f\u043e\u0434\u0440\u0435\u0434\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0441\u043f\u043e\u0440\u0435\u0434 \u0442\u043e\u0432\u0430 \u043a\u043e\u043b\u043a\u043e \u0441\u0438\u043b\u043d\u043e \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435. \u0422\u043e\u0432\u0430 \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0434\u0430 \u0441\u0435 \u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u0446\u0438\u0440\u0430\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438, \u043a\u043e\u0438\u0442\u043e \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u043f\u043e-\u0432\u0430\u0436\u043d\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u043e \u0437\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f.\n\n- **\u0414\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u043e\u043d\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437:** \u041f\u0440\u043e\u0432\u0435\u0434\u0435\u043d \u0435 ANOVA \u0442\u0435\u0441\u0442, \u0437\u0430 \u0434\u0430 \u0441\u0435 \u043f\u0440\u043e\u0432\u0435\u0440\u0438 \u0434\u0430\u043b\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\u0442\u0435 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u0441\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u0430\u0432\u0430\u0442 \u043c\u0435\u0436\u0434\u0443 \u0433\u0440\u0443\u043f\u0438\u0442\u0435 (\u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435). \u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0440\u0430\u0437\u043b\u0438\u043a\u0438\u0442\u0435 \u043c\u0435\u0436\u0434\u0443 \u0433\u0440\u0443\u043f\u0438\u0442\u0435 \u0441\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u043d\u0430\u0447\u0438\u043c\u0438. \u0421\u043b\u0435\u0434 \u0442\u043e\u0432\u0430 \u0447\u0440\u0435\u0437 Tukey HSD \u0435 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430\u043d\u043e \u043c\u0435\u0436\u0434\u0443 \u043a\u043e\u0438 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u0438 \u0433\u0440\u0443\u043f\u0438 \u0441\u0435 \u043d\u0430\u0431\u043b\u044e\u0434\u0430\u0432\u0430\u0442 \u0442\u0435\u0437\u0438 \u0440\u0430\u0437\u043b\u0438\u043a\u0438. \u0410\u043d\u0430\u043b\u0438\u0437\u044a\u0442, \u0438\u0437\u0432\u044a\u0440\u0448\u0435\u043d \u0432\u044a\u0440\u0445\u0443 \u0434\u0432\u0430\u0442\u0430 \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u043a\u0430 \u0441\u043f\u043e\u0440\u0435\u0434 eta-squared, \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0432 \u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u0441\u043b\u0443\u0447\u0430\u0438 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0438\u043c\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0437\u043d\u0430\u0447\u0438\u043c\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f.\n\n**\u0418\u0437\u0432\u043e\u0434 \u043d\u0430 \u043d\u0438\u0432\u043e EDA:** \u0414\u0430\u043d\u043d\u0438\u0442\u0435 \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430\u0442 \u0447\u0438\u0441\u0442\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438 \u0437\u0430 \u043f\u0440\u043e\u0435\u043a\u0442\u0430; \u0438\u043c\u0430 \u044f\u0441\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u0438\u044f. \u0422\u0435\u0437\u0438 \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f \u0434\u0430\u0432\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430 \u043f\u0440\u0438\u043b\u0430\u0433\u0430\u043d\u0435 \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043d\u0435 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435."
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

# %% [markdown] cell_id="da51c40b29034890a194fef1f1a2965c" deepnote_block_group="735b51333cc849ffa05cde6fa3ebbd9c" deepnote_cell_type="markdown" deepnote_sorting_key="40" deepnote_source="## \u041a\u0440\u0430\u0442\u043a\u043e \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043d\u0430 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435, \u043a\u043e\u0438\u0442\u043e \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435\n\n\u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u0449\u0435 \u0432\u043a\u043b\u044e\u0447\u0432\u0430 \u0434\u0432\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 ML \u0437\u0430\u0434\u0430\u0447\u0438 \u0432\u044a\u0440\u0445\u0443 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 \u0441 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438: **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440** \u0438 **\u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435/\u0435\u043c\u043e\u0446\u0438\u043e\u043d\u0430\u043b\u0435\u043d \u043f\u0440\u043e\u0444\u0438\u043b**. \u0412\u0441\u0438\u0447\u043a\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u0438 \u0441\u0442\u044a\u043f\u043a\u0438 \u0449\u0435 \u0431\u044a\u0434\u0430\u0442 \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d\u0438 \u0441\u044a\u0441 `scikit-learn` \u0438 \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438 \u0442\u0435\u0445\u043d\u0438\u043a\u0438 \u043e\u0442 \u043a\u0443\u0440\u0441\u0430.\n\n### \u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u043c\u0443\u0437\u0438\u043a\u0430\u043b\u0435\u043d \u0436\u0430\u043d\u0440 (supervised learning)\n\u0429\u0435 \u0442\u0440\u0435\u0442\u0438\u0440\u0430\u043c\u0435 \u043a\u043e\u043b\u043e\u043d\u0430\u0442\u0430 **`track_genre`** \u043a\u0430\u0442\u043e \u0446\u0435\u043b\u0435\u0432\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0438 \u0449\u0435 \u043e\u0431\u0443\u0447\u0438\u043c \u043c\u043e\u0434\u0435\u043b\u0438, \u043a\u043e\u0438\u0442\u043e \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u0442 \u0436\u0430\u043d\u0440\u0430 \u043d\u0430 \u043f\u0435\u0441\u0435\u043d\u0442\u0430 \u043f\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043d\u0430\u043f\u0440. `danceability`, `energy`, `acousticness`, `valence`, `tempo` \u0438 \u0434\u0440.).\n\n\u041f\u043b\u0430\u043d\u0438\u0440\u0430\u043c\u0435 \u0434\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u043c \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u044a\u043c\u0430:\n- **Logistic Regression** (\u0431\u0430\u0437\u043e\u0432 \u043c\u043e\u0434\u0435\u043b);\n- **k-Nearest Neighbors (kNN)**;\n- **Support Vector Machines (SVM)**;\n- **Decision Tree / Random Forest** (\u0437\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0438 \u043f\u043e-\u043b\u0435\u0441\u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f);\n- **MLPClassifier** \u043a\u0430\u0442\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u043e\u0442 \u0443\u0447\u0435\u0431\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b.\n\n\u0429\u0435 \u043f\u0440\u0438\u043b\u043e\u0436\u0438\u043c \u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0438 \u043f\u0440\u0430\u043a\u0442\u0438\u043a\u0438 \u0437\u0430 \u043d\u0430\u0434\u0435\u0436\u0434\u043d\u0430 \u043e\u0446\u0435\u043d\u043a\u0430:\n- \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u043d\u0430 train/test \u0438/\u0438\u043b\u0438 **cross-validation**;\n- \u043f\u043e\u0434\u0431\u043e\u0440 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0447\u0440\u0435\u0437 **GridSearchCV** \u0438\u043b\u0438 **RandomizedSearchCV**;\n- \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043a\u0430\u0442\u043e **accuracy**, **macro F1**, **Precision**, **Recall** \u0438 **confusion matrix** (\u043e\u0441\u043e\u0431\u0435\u043d\u043e \u0432\u0430\u0436\u043d\u0438 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u043a\u043b\u0430\u0441\u043e\u0432\u0435).\n\n### \u041a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0435\u0441\u043d\u0438 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 (unsupervised learning)\n\u0417\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u043f\u043e \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u0431\u0435\u0437 \u0436\u0430\u043d\u0440\u043e\u0432\u0438\u0442\u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u0438), \u0437\u0430 \u0434\u0430 \u0433\u0440\u0443\u043f\u0438\u0440\u0430\u043c\u0435 \u043f\u0435\u0441\u043d\u0438 \u0441\u044a\u0441 \u0441\u0445\u043e\u0434\u0435\u043d \u043f\u0440\u043e\u0444\u0438\u043b.\n\n\u041f\u043b\u0430\u043d\u0438\u0440\u0430\u043c\u0435 \u0434\u0430 \u0438\u0437\u043f\u0440\u043e\u0431\u0432\u0430\u043c\u0435:\n- **KMeans** (\u043e\u0441\u043d\u043e\u0432\u0435\u043d \u043c\u0435\u0442\u043e\u0434);\n- **DBSCAN** (\u0437\u0430 \u043e\u0442\u043a\u0440\u0438\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u043e-\u0441\u043b\u043e\u0436\u043d\u0438 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438 \u0438 \u043f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u0438 \u0430\u0443\u0442\u043b\u0430\u0439\u0435\u0440\u0438);\n- *(\u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e \u0440\u0430\u0437\u0448\u0438\u0440\u0435\u043d\u0438\u0435)* **Agglomerative Clustering** \u043a\u0430\u0442\u043e \u0430\u043b\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u0430 \u043d\u0430 KMeans/DBSCAN.\n\n\u0417\u0430 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0438 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0442\u0435 \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u0438 \u043e\u0442 `scikit-learn`, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:\n- **silhouette score**, **Davies\u2013Bouldin index** \u0438/\u0438\u043b\u0438 **Calinski\u2013Harabasz score** (\u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u043d\u0430 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u044f);\n- \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0442\u0435 \u0447\u0440\u0435\u0437 **\u0441\u0440\u0435\u0434\u043d\u0438/\u043c\u0435\u0434\u0438\u0430\u043d\u0438 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435** \u043f\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440 \u0438 \u043e\u043f\u0438\u0441\u0432\u0430\u043d\u0435 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438 \u201e\u043f\u0440\u043e\u0444\u0438\u043b\u0438\u201c (\u043d\u0430\u043f\u0440. \u043f\u043e `energy` \u0438 `valence`).\n\n\u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e, \u0437\u0430 \u043f\u043e-\u044f\u0441\u043d\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043c\u0435\u0442\u043e\u0434\u0438 \u0437\u0430 \u043f\u043e\u043d\u0438\u0436\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u0440\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u0442\u0430:\n- **PCA** (2D/3D \u043f\u0440\u043e\u0435\u043a\u0446\u0438\u044f \u0437\u0430 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0430 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430\u0442\u0430),\n- *(\u043f\u043e \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442)* **t-SNE** \u043a\u0430\u0442\u043e \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u0430 \u0442\u0435\u0445\u043d\u0438\u043a\u0430 (\u0441\u0430\u043c\u043e \u0437\u0430 \u0438\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f, \u043d\u0435 \u043a\u0430\u0442\u043e \u043c\u043e\u0434\u0435\u043b).\n"
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

# %% [markdown] cell_id="473f3aba4bba4273aabab54cfc8c97c3" deepnote_block_group="247ae8135cfb41ee90716f6e303db8d1" deepnote_cell_type="markdown" deepnote_sorting_key="41" deepnote_source="## \u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 \u0438 \u0442\u0435\u0445\u043d\u043e\u043b\u043e\u0433\u0438\u0438, \u043a\u043e\u0438\u0442\u043e \u0441\u043c\u044f\u0442\u0430\u043c\u0435 \u0434\u0430 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435\n\n\u041f\u0440\u043e\u0435\u043a\u0442\u044a\u0442 \u0449\u0435 \u0431\u044a\u0434\u0435 \u0440\u0435\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d \u043d\u0430 **Python** \u0441 **Jupyter Notebook**, \u043a\u0430\u0442\u043e \u0449\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043c\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u0438 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0438 \u043e\u0442 \u0435\u043a\u043e\u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0442\u0430 \u0437\u0430 \u0440\u0430\u0431\u043e\u0442\u0430 \u0441 \u0442\u0430\u0431\u043b\u0438\u0447\u043d\u0438 \u0434\u0430\u043d\u043d\u0438 \u0438 `scikit-learn`:\n\n- **NumPy** \u2013 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0438 \u043c\u0430\u0441\u0438\u0432\u0438;\n- **Pandas** \u2013 \u0437\u0430\u0440\u0435\u0436\u0434\u0430\u043d\u0435 \u0438 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (`CSV`), \u0444\u0438\u043b\u0442\u0440\u0438\u0440\u0430\u043d\u0435, \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438;\n- **Matplotlib** \u0438 **Seaborn** \u2013 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u0437\u0430 EDA \u0438 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435;\n- **Scikit-learn** \u2013 \u043e\u0441\u043d\u043e\u0432\u043d\u0430\u0442\u0430 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0430 \u0437\u0430 \u0446\u0435\u043b\u0438\u044f ML pipeline:\n  - \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430: `StandardScaler` / `MinMaxScaler`, `LabelEncoder` / `OneHotEncoder` (\u0430\u043a\u043e \u0435 \u043d\u0443\u0436\u043d\u043e),\n  - \u043c\u043e\u0434\u0435\u043b\u0438: Logistic Regression, kNN, SVM, Decision Tree / Random Forest, KMeans, DBSCAN (\u0438 \u0435\u0432\u0435\u043d\u0442\u0443\u0430\u043b\u043d\u043e Agglomerative),\n  - \u043e\u0446\u0435\u043d\u043a\u0430: \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f,\n  - \u0432\u0430\u043b\u0438\u0434\u0430\u0446\u0438\u044f \u0438 tuning: `train_test_split`, `cross_val_score`, `GridSearchCV` / `RandomizedSearchCV`,\n  - **Pipeline** \u0438 **ColumnTransformer** (\u0437\u0430 \u043f\u043e-\u0447\u0438\u0441\u0442 \u0438 \u0432\u044a\u0437\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u043c \u043a\u043e\u0434);\n- *(\u0430\u043a\u043e \u0435 \u043d\u0443\u0436\u043d\u043e \u0437\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0430 \u0447\u0430\u0441\u0442 \u043a\u0430\u0442\u043e \u043f\u0440\u0438 preliminary analysis)* **Statsmodels** \u2013 \u0437\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u0438 \u0442\u0435\u0441\u0442\u043e\u0432\u0435 \u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438;\n- **kagglehub** \u2013 \u0437\u0430 \u0438\u0437\u0442\u0435\u0433\u043b\u044f\u043d\u0435 \u043d\u0430 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438 \u043e\u0442 Kaggle \u0432 \u0440\u0430\u0431\u043e\u0442\u043d\u0430\u0442\u0430 \u0441\u0440\u0435\u0434\u0430."
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

# %% [markdown] cell_id="77592aa4510e4f6e9751c1531116a45b" deepnote_block_group="009a9d14cba44937acad976795bbd4d7" deepnote_cell_type="markdown" deepnote_sorting_key="42" deepnote_source="# \u0427\u0430\u0441\u0442 1: \u041a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u2013 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\n\n\u0412 \u043f\u044a\u0440\u0432\u0430\u0442\u0430 \u0447\u0430\u0441\u0442 \u0441\u0435 \u0440\u0430\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043f\u043e **\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f**, \u043f\u0440\u0438 \u043a\u043e\u044f\u0442\u043e \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430 \u0436\u0430\u043d\u0440\u044a\u0442 (`track_genre`) \u043d\u0430 \u0434\u0430\u0434\u0435\u043d\u0430 \u043f\u0435\u0441\u0435\u043d \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043a\u0430\u0442\u043e *danceability, energy, acousticness, valence* \u0438 \u0434\u0440.  \n\u0426\u0435\u043b\u0442\u0430 \u0435 \u0434\u0430 \u0441\u0435 \u0441\u0440\u0430\u0432\u043d\u044f\u0442 \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u0438 \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u043a\u043e\u0438 \u043e\u0442 \u0442\u044f\u0445 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0435 \u0437\u0430 \u0442\u0430\u0437\u0438 \u0437\u0430\u0434\u0430\u0447\u0430.\n"
# # Част 1: Класификационна задача – предсказване на жанр
#
# В първата част се разглежда задача по **класификация**, при която се предсказва жанрът (`track_genre`) на дадена песен на база числови аудио признаци като *danceability, energy, acousticness, valence* и др.  
# Целта е да се сравнят класически алгоритми за класификация и да се оцени кои от тях се справят най-добре за тази задача.
#

# %% [markdown] cell_id="dfbc1df9dbf0465e99cada405b2926d0" deepnote_block_group="620684948d48433fb4cd2c223ad9f403" deepnote_cell_type="markdown" deepnote_sorting_key="43" deepnote_source="## \u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u043d\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (\u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f)\n\n\u041f\u0440\u0435\u0434\u0438 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435\u0442\u043e \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438 \u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0434\u0430\u043d\u043d\u0438\u0442\u0435 \u0434\u0430 \u0441\u0435 \u043f\u043e\u0434\u0433\u043e\u0442\u0432\u044f\u0442 \u0442\u0430\u043a\u0430, \u0447\u0435 \u0434\u0430 \u0441\u0430 \u043a\u043e\u0440\u0435\u043a\u0442\u043d\u0438 \u0438 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0438 \u0437\u0430 ML \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438:\n\n- **\u041f\u043e\u0447\u0438\u0441\u0442\u0432\u0430\u043d\u0435**: \u043f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u0434\u0443\u0431\u043b\u0438\u0440\u0430\u043d\u0438 \u0437\u0430\u043f\u0438\u0441\u0438 \u0438 \u0440\u0435\u0434\u043e\u0432\u0435 \u0441 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0438\u043b\u0438 \u0437\u0430\u043f\u044a\u043b\u0432\u0430\u043d\u0435 \u043f\u0440\u0438 \u043d\u0443\u0436\u0434\u0430)\n- **\u0422\u0438\u043f\u043e\u0432\u0435 \u0434\u0430\u043d\u043d\u0438**: \u043f\u0440\u043e\u0432\u0435\u0440\u044f\u0432\u0430 \u0441\u0435 \u0442\u0438\u043f\u044a\u0442 \u043d\u0430 \u043a\u043e\u043b\u043e\u043d\u0438\u0442\u0435 \u0438 \u043f\u0440\u0438 \u043d\u0443\u0436\u0434\u0430 \u0441\u0435 \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u0443\u0432\u0430\u0442 \u0432 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\n- **\u0418\u0437\u0431\u043e\u0440 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 (features)**: \u0432 \u043c\u043e\u0434\u0435\u043b\u0430 \u0441\u0435 \u0432\u043a\u043b\u044e\u0447\u0432\u0430\u0442 \u0441\u0430\u043c\u043e \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430, \u043d\u0430\u043f\u0440. danceability, energy, loudness) \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d \u0431\u0440\u043e\u0439 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 (\u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043a\u043e\u043b\u043e\u043d\u0438, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0430 \u0438\u0437\u0432\u043b\u0435\u0447\u0435\u043d\u0438 \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430, \u043d\u0430\u043f\u0440. popularity, duration_ms). \u0422\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u043f\u043e\u043b\u0435\u0442\u0430 (\u043d\u0430\u043f\u0440. \u0438\u043c\u0435 \u043d\u0430 \u043f\u0435\u0441\u0435\u043d/\u0438\u0437\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b) \u043d\u0435 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0438\u0437\u0438\u0441\u043a\u0432\u0430\u0442 \u043e\u0442\u0434\u0435\u043b\u0435\u043d \u043f\u043e\u0434\u0445\u043e\u0434 \u0437\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430 \u0442\u0435\u043a\u0441\u0442.\n- **\u0420\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 train/test**: \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435\u0442\u043e \u0435 \u0441\u0442\u0440\u0430\u0442\u0438\u0444\u0438\u0446\u0438\u0440\u0430\u043d\u043e \u043f\u043e track_genre, \u0442\u0430\u043a\u0430 \u0447\u0435 \u0432\u0441\u0435\u043a\u0438 \u0436\u0430\u043d\u0440 \u0434\u0430 \u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0435\u043d \u0441\u0445\u043e\u0434\u043d\u043e \u0432 \u043e\u0431\u0443\u0447\u0430\u0432\u0430\u0449\u0438\u044f \u0438 \u0442\u0435\u0441\u0442\u043e\u0432\u0438\u044f \u043d\u0430\u0431\u043e\u0440\n- **\u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f (scaling)**: \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u0441\u0435 `StandardScaler`, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0447\u0430\u0441\u0442 \u043e\u0442 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 (\u043d\u0430\u043f\u0440. Logistic Regression, kNN, SVM) \u0441\u0430 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u043d\u0438 \u043a\u044a\u043c \u043c\u0430\u0449\u0430\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435. \u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 `Pipeline`, \u0437\u0430 \u0434\u0430 \u0441\u0435 \u0438\u0437\u0431\u0435\u0433\u043d\u0435 data leakage (scaler \u0441\u0435 \u043e\u0431\u0443\u0447\u0430\u0432\u0430 \u0441\u0430\u043c\u043e \u0432\u044a\u0440\u0445\u0443 train \u0447\u0430\u0441\u0442\u0442\u0430)\n\n**\u0420\u0430\u0437\u043b\u0438\u043a\u0430 \u0441\u043f\u0440\u044f\u043c\u043e \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430:** \u043f\u0440\u0438 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u044f\u043c\u0430 \u0446\u0435\u043b\u0435\u0432\u0430 \u043f\u0440\u043e\u043c\u0435\u043d\u043b\u0438\u0432\u0430 \u0438 \u043d\u044f\u043c\u0430 train/test split \u0432 \u0441\u044a\u0449\u0438\u044f \u0441\u043c\u0438\u0441\u044a\u043b; scaling \u0435 \u043e\u0449\u0435 \u043f\u043e-\u0432\u0430\u0436\u0435\u043d, \u0437\u0430\u0449\u043e\u0442\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435 \u0441\u0430 distance-based; \u0437\u0430 \u043a\u043b\u044a\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u0441\u0435 \u043f\u043e\u0434\u0431\u0438\u0440\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u043d\u043e \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438, \u0441\u0432\u044a\u0440\u0437\u0430\u043d\u0438 \u0441\u044a\u0441 \u0437\u0432\u0443\u0447\u0435\u043d\u0435 \u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435, \u0432\u043c\u0435\u0441\u0442\u043e \u0432\u0441\u0438\u0447\u043a\u0438 \u043d\u0430\u043b\u0438\u0447\u043d\u0438 \u043a\u043e\u043b\u043e\u043d\u0438.\n"
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

# %% cell_id="1f2ce432efe540e2a6ada68c11b3e228" deepnote_block_group="636ac9ebc27b4152a9e5e156f8754ecc" deepnote_cell_type="code" deepnote_content_hash="c085b6ba" deepnote_execution_finished_at="2026-01-27T20:26:37.212Z" deepnote_execution_started_at="2026-01-27T20:26:37.211Z" deepnote_sorting_key="44" deepnote_source="df.head()" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1 execution_start=1769545597211 source_hash="c085b6ba"
df.head()

# %% cell_id="9491e29799d0492ea3cc4c36171a4946" deepnote_block_group="5bed78181ff440708e16d2a98e89a69a" deepnote_cell_type="code" deepnote_content_hash="20c58c7b" deepnote_execution_finished_at="2026-01-27T21:47:25.112Z" deepnote_execution_started_at="2026-01-27T21:47:24.981Z" deepnote_sorting_key="45" deepnote_source="df_cls = df.copy()\n\n# \u041f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u044a\u043b\u043d\u0438 \u0434\u0443\u0431\u043b\u0438\u043a\u0430\u0442\u0438\ndf_cls = df_cls.drop_duplicates()\n\n# \u041f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u043d\u0435 \u043d\u0430 \u0440\u0435\u0434\u043e\u0432\u0435 \u0441 \u043b\u0438\u043f\u0441\u0432\u0430\u0449\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0432 \u0442\u043e\u0437\u0438 dataset \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0441\u0430 \u043c\u043d\u043e\u0433\u043e \u043c\u0430\u043b\u043a\u043e)\ndf_cls = df_cls.dropna()\n\n# explicit \u043f\u0440\u0435\u043e\u0431\u0440\u0430\u0437\u0443\u0432\u0430\u043c\u0435 \u043a\u044a\u043c 0/1 (int)\nif \"explicit\" in df_cls.columns:\n    df_cls[\"explicit\"] = df_cls[\"explicit\"].astype(int)\n\ndf_cls.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=131 execution_start=1769550444981 source_hash="20c58c7b"
df_cls = df.copy()

# Премахване на пълни дубликати
df_cls = df_cls.drop_duplicates()

# Премахване на редове с липсващи стойности (в този dataset обикновено са много малко)
df_cls = df_cls.dropna()

# explicit преобразуваме към 0/1 (int)
if "explicit" in df_cls.columns:
    df_cls["explicit"] = df_cls["explicit"].astype(int)

df_cls.shape

# %% cell_id="135b2534d65449b6a51cf11f3e91a374" deepnote_block_group="1ac4a0fba2924737a181b67330104066" deepnote_cell_type="code" deepnote_content_hash="b4e731c" deepnote_execution_finished_at="2026-01-27T21:47:27.568Z" deepnote_execution_started_at="2026-01-27T21:47:27.524Z" deepnote_sorting_key="46" deepnote_source="target_col = \"track_genre\"\n\n# \u0417\u0430 features \u0438\u043c\u0430\u043c\u0435 \u0434\u0432\u0430 \u0442\u0438\u043f\u0430: \n# A\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043e\u043f\u0438\u0441\u0432\u0430\u0442 \u0437\u0432\u0443\u0447\u0435\u043d\u0435/\u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435) - \u043d\u0430\u043f\u0440. danceability, energy, loudness, speechiness, acousticness\n# \u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 (\u043d\u0435 \u0441\u0430 \u0434\u0438\u0440\u0435\u043a\u0442\u043d\u043e \u043e\u0442 \u0430\u0443\u0434\u0438\u043e \u0441\u0438\u0433\u043d\u0430\u043b\u0430) - \u043d\u0430\u043f\u0440. popularity, duration_ms, explicit\n# \u041c\u0430\u0445\u0430\u043c\u0435 id, \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u043f\u043e\u043b\u0435\u0442\u0430 \u0438 key_name (\u0434\u0443\u0431\u043b\u0438\u0440\u0430 key, \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435)\ndrop_cols = [\n    \"track_id\", \"artists\", \"album_name\", \"track_name\", \"key_name\"\n]\n\nfeature_cols = [c for c in df.columns if c not in drop_cols + [target_col]]\nfeature_cols\n\ndf_cls = df_cls[feature_cols + [target_col]].copy()\n\ndf_cls.head()" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=44 execution_start=1769550447524 source_hash="b4e731c"
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

# %% cell_id="3660c1bb0d074bb8a881d7a055336e87" deepnote_block_group="d9c3364dd18348eab5f57b2d14b5cee7" deepnote_cell_type="code" deepnote_content_hash="2e3daa39" deepnote_execution_finished_at="2026-01-27T21:47:29.981Z" deepnote_execution_started_at="2026-01-27T21:47:29.911Z" deepnote_sorting_key="47" deepnote_source="# Train/test split \u0441\u044a\u0441 \u0441\u0442\u0440\u0430\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f\nX = df_cls[feature_cols]\ny = df_cls[target_col]\n\nX_train, X_test, y_train, y_test = train_test_split(\n    X, y,\n    test_size=0.2,\n    random_state=67,\n    stratify=y\n)\n\nX_train.shape, X_test.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=70 execution_start=1769550449911 source_hash="2e3daa39"
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

# %% cell_id="e9daa02d06fd4ae5bd38c902b26bee9c" deepnote_block_group="2b39457c78d047b0bac78b9016db326d" deepnote_cell_type="code" deepnote_content_hash="288c6149" deepnote_execution_finished_at="2026-01-27T21:47:33.063Z" deepnote_execution_started_at="2026-01-27T21:47:33.058Z" deepnote_sorting_key="48" deepnote_source="# \u041d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f (scaling)\n\n# ColumnTransformer \u043f\u0440\u0438\u043b\u0430\u0433\u0430 \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u0432\u044a\u0440\u0445\u0443 \u0433\u0440\u0443\u043f\u0438 \u043a\u043e\u043b\u043e\u043d\u0438 (\u0442\u0443\u043a: \u0432\u044a\u0440\u0445\u0443 feature_cols)\n# \"num\" \u0435 \u0435\u0442\u0438\u043a\u0435\u0442\u044a\u0442 \u043d\u0430 \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f\u0442\u0430 \u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438\u0442\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\npreprocess_cls = ColumnTransformer(\n    transformers=[\n        (\"num\", StandardScaler(), feature_cols)\n    ],\n    remainder=\"drop\" # \u0412\u0441\u0438\u0447\u043a\u0438 \u043a\u043e\u043b\u043e\u043d\u0438, \u043a\u043e\u0438\u0442\u043e \u043d\u0435 \u0441\u0430 \u0432 feature_cols, \u0441\u0435 \u043f\u0440\u0435\u043c\u0430\u0445\u0432\u0430\u0442\n)\n\npreprocess_cls" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=5 execution_start=1769550453058 source_hash="288c6149"
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

# %% cell_id="bb08665690ae4df286af102943dafba5" deepnote_block_group="8ce98f1aa606430d8b05e62221643241" deepnote_cell_type="code" deepnote_content_hash="e5e4d9b6" deepnote_execution_finished_at="2026-01-27T21:47:37.245Z" deepnote_execution_started_at="2026-01-27T21:47:37.210Z" deepnote_sorting_key="49" deepnote_source="# \u041f\u0440\u0438\u043b\u0430\u0433\u0430\u043d\u0435 \u043d\u0430 \u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430\nX_train_scaled = preprocess_cls.fit_transform(X_train)\nX_test_scaled = preprocess_cls.transform(X_test)\n\nX_train_scaled.shape, X_test_scaled.shape" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=35 execution_start=1769550457210 source_hash="e5e4d9b6"
# Прилагане на нормализацията
X_train_scaled = preprocess_cls.fit_transform(X_train)
X_test_scaled = preprocess_cls.transform(X_test)

X_train_scaled.shape, X_test_scaled.shape

# %% [markdown] cell_id="837b588f61df4fd2b7fac1669bfd358a" deepnote_block_group="6a49fce0cee44b43ac1ff6690f7ffec2" deepnote_cell_type="markdown" deepnote_sorting_key="50" deepnote_source="## \u041c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u043d\u0435 \u043d\u0430 \u0434\u0430\u043d\u043d\u0438\u0442\u0435 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f)\n\n\u0412 \u0442\u0430\u0437\u0438 \u0441\u0435\u043a\u0446\u0438\u044f \u0441\u0435 \u043e\u0431\u0443\u0447\u0430\u0432\u0430\u0442 \u0438 \u0441\u0440\u0430\u0432\u043d\u044f\u0432\u0430\u0442 \u043d\u044f\u043a\u043e\u043b\u043a\u043e \u043a\u043b\u0430\u0441\u0438\u0447\u0435\u0441\u043a\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u044a\u043c\u0430 \u0437\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 `track_genre` \u043d\u0430 \u0431\u0430\u0437\u0430 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438.  \n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 \u0435\u0434\u0438\u043d \u0438 \u0441\u044a\u0449 preprocessing pipeline (\u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u0441\u044a\u0441 `StandardScaler`), \u0437\u0430 \u0434\u0430 \u0441\u0430 \u043a\u043e\u0440\u0435\u043a\u0442\u043d\u0438 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f\u0442\u0430.  \n\u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0441\u0435 \u043e\u0446\u0435\u043d\u044f\u0432\u0430\u0442 \u043a\u0430\u043a\u0442\u043e \u043d\u0430 \u0442\u0435\u0441\u0442\u043e\u0432 \u043d\u0430\u0431\u043e\u0440, \u0442\u0430\u043a\u0430 \u0438 \u0447\u0440\u0435\u0437 cross-validation. \u0417\u0430 \u0447\u0430\u0441\u0442 \u043e\u0442 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 \u0441\u0435 \u043f\u0440\u0430\u0432\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 \u0447\u0440\u0435\u0437 `GridSearchCV`.\n"
# ## Моделиране на данните (класификация)
#
# В тази секция се обучават и сравняват няколко класически алгоритъма за класификация на `track_genre` на база числови аудио характеристики.  
# Използва се един и същ preprocessing pipeline (нормализация със `StandardScaler`), за да са коректни сравненията.  
# Резултатите се оценяват както на тестов набор, така и чрез cross-validation. За част от моделите се прави настройка на хиперпараметри чрез `GridSearchCV`.
#

# %% cell_id="6d444fef01a746c98565ab1363e1914e" deepnote_block_group="30ada9136e4e46a4a05c2289d56651a1" deepnote_cell_type="code" deepnote_content_hash="eee912e0" deepnote_execution_finished_at="2026-01-27T21:24:44.449Z" deepnote_execution_started_at="2026-01-27T21:24:44.447Z" deepnote_sorting_key="51" deepnote_source="print(\"\u041e\u0431\u0449 \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435:\", df[\"track_genre\"].nunique())" execution_context_id="4c6b5e76-66bb-4d77-99bd-b33de1734382" execution_millis=2 execution_start=1769549084447 source_hash="eee912e0"
print("Общ брой жанрове:", df["track_genre"].nunique())

# %% [markdown] cell_id="209916747cdd40b1bcc11cb7b8557c6e" deepnote_block_group="8abac77f0d9548c3ab379129abff5a0f" deepnote_cell_type="markdown" deepnote_sorting_key="52" deepnote_source="### \u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0438\u0437\u0431\u043e\u0440\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 (feature selection)\n\n\u0421 \u0446\u0435\u043b \u0434\u0430 \u0441\u0435 \u043e\u0446\u0435\u043d\u0438 \u0432\u043b\u0438\u044f\u043d\u0438\u0435\u0442\u043e \u043d\u0430 \u0438\u0437\u0431\u043e\u0440\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0432\u044a\u0440\u0445\u0443 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f\u0442\u0430, \u0431\u044f\u0445\u0430 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438 \u0442\u0440\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u043d\u0430\u0431\u043e\u0440\u0430 \u043e\u0442 features:  \n(1) \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043e\u0442 \u043d\u0430\u0439-\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u0438\u0442\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u0441\u043f\u043e\u0440\u0435\u0434 EDA,  \n(2) \u0441\u044a\u0449\u043e\u0442\u043e \u043f\u043e\u0434\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0441 \u0434\u043e\u0431\u0430\u0432\u0435\u043d\u043e \u0442\u0435\u043c\u043f\u043e (`tempo`),  \n(3) \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u0432\u0441\u0438\u0447\u043a\u0438 \u043d\u0430\u043b\u0438\u0447\u043d\u0438 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438.\n\n\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435\u0442\u043e \u0435 \u043d\u0430\u043f\u0440\u0430\u0432\u0435\u043d\u043e \u0447\u0440\u0435\u0437 cross-validation \u0441 Logistic Regression \u0438 \u043c\u0435\u0442\u0440\u0438\u043a\u0430 **Macro F1**, \u043a\u043e\u044f\u0442\u043e \u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0430 \u0437\u0430 \u043c\u043d\u043e\u0433\u043e-\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f.\n\n\u0420\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0441 \u043f\u044a\u043b\u043d\u0438\u044f \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e-\u0432\u0438\u0441\u043e\u043a Macro F1 \u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0449\u0438 \u0441\u0430\u043c\u043e \u043d\u0430\u0439-\u0441\u0438\u043b\u043d\u0438\u0442\u0435 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438 \u0441\u043f\u043e\u0440\u0435\u0434 EDA. \u0422\u043e\u0432\u0430 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438\u0442\u0435 \u0447\u0438\u0441\u043b\u043e\u0432\u0438 \u0430\u0442\u0440\u0438\u0431\u0443\u0442\u0438 \u0434\u043e\u043f\u0440\u0438\u043d\u0430\u0441\u044f\u0442 \u0437\u0430 \u043f\u043e-\u0434\u043e\u0431\u0440\u043e \u0440\u0430\u0437\u0433\u0440\u0430\u043d\u0438\u0447\u0430\u0432\u0430\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n\n\u0412 \u0441\u043b\u0435\u0434\u0432\u0430\u0449\u0438\u0442\u0435 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0438 \u0441\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440 \u043e\u0442 features.\n"
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

# %% cell_id="68be52c289094b74ad75e89811229517" deepnote_block_group="eec6ace5cc844f078d0b397b3c25eba6" deepnote_cell_type="code" deepnote_content_hash="9d3207c4" deepnote_execution_finished_at="2026-01-27T20:26:37.771Z" deepnote_execution_started_at="2026-01-27T20:26:37.771Z" deepnote_sorting_key="53" deepnote_source="# Feature set 1: \u0442\u043e\u043f \u0441\u043f\u043e\u0440\u0435\u0434 EDA\nfeatures_eda_top = [\n    \"acousticness\",\"energy\",\"instrumentalness\",\"loudness\",\n    \"speechiness\",\"danceability\",\"valence\",\"liveness\"\n]\n\n# Feature set 2: + tempo\nfeatures_eda_top_plus = features_eda_top + [\"tempo\"]\n\n# Feature set 3: \u043f\u044a\u043b\u043d\u0438\u044f\u0442 \u043d\u0430\u0431\u043e\u0440\nfeatures_full = feature_cols  # \u043e\u0442 \u0442\u0432\u043e\u044f preprocessing" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=0 execution_start=1769545597771 source_hash="9d3207c4"
# Feature set 1: топ според EDA
features_eda_top = [
    "acousticness","energy","instrumentalness","loudness",
    "speechiness","danceability","valence","liveness"
]

# Feature set 2: + tempo
features_eda_top_plus = features_eda_top + ["tempo"]

# Feature set 3: пълният набор
features_full = feature_cols  # от твоя preprocessing


# %% cell_id="60f098e4e9154742b5e08806813f2e1b" deepnote_block_group="6c74508e25d04149906459595b74c454" deepnote_cell_type="code" deepnote_content_hash="5f47b7cf" deepnote_execution_finished_at="2026-01-27T20:30:24.261Z" deepnote_execution_started_at="2026-01-27T20:26:37.831Z" deepnote_sorting_key="54" deepnote_source="def cv_macro_f1(df, features, target=\"track_genre\", cv=3):\n    X = df[features]\n    y = df[target]\n\n    model = Pipeline([\n        (\"scale\", StandardScaler()),\n        (\"clf\", LogisticRegression(max_iter=2000))\n    ])\n\n    scores = cross_val_score(model, X, y, scoring=\"f1_macro\", cv=cv, n_jobs=-1)\n    return scores.mean(), scores.std()\n\n\nfeature_sets = {\n    \"EDA top\": features_eda_top,\n    \"EDA top + tempo\": features_eda_top_plus,\n    \"Full features\": feature_cols\n}\n\nfor name, feats in feature_sets.items():\n    mean_f1, std_f1 = cv_macro_f1(df, feats)\n    print(f\"{name:15s} -> Macro F1: {mean_f1:.4f} \u00b1 {std_f1:.4f}\")" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=226430 execution_start=1769545597831 source_hash="5f47b7cf"
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


# %% [markdown] cell_id="ff8dff9d286f493bbafc07be58f81092" deepnote_block_group="97ca620f3e224923aa5a79985ead4cf1" deepnote_cell_type="markdown" deepnote_sorting_key="55" deepnote_source="### \u041e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435\n\n\u0417\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u0438\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u0435 \u0434\u0435\u0444\u0438\u043d\u0438\u0440\u0430\u043d\u0430 \u043e\u0431\u0449\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f, \u043a\u043e\u044f\u0442\u043e \u0438\u0437\u0432\u044a\u0440\u0448\u0432\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435, \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435 \u0438 \u0438\u0437\u0447\u0438\u0441\u043b\u044f\u0432\u0430\u043d\u0435 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u043d\u0438\u0442\u0435 \u043c\u0435\u0442\u0440\u0438\u043a\u0438 \u0437\u0430 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u043e.  \n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u0442 \u0441\u0435 **Accuracy** \u0438 **Macro F1**, \u043a\u0430\u0442\u043e Macro F1 \u0435 \u0432\u043e\u0434\u0435\u0449\u0430\u0442\u0430 \u043c\u0435\u0442\u0440\u0438\u043a\u0430 \u043f\u043e\u0440\u0430\u0434\u0438 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0438\u044f \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440 \u043d\u0430 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430.\n\n\u0424\u0443\u043d\u043a\u0446\u0438\u044f\u0442\u0430 \u0438\u0437\u0432\u0435\u0436\u0434\u0430 \u0438 **classification report** \u0441 Precision, Recall \u0438 F1-score \u0437\u0430 \u0432\u0441\u0435\u043a\u0438 \u0436\u0430\u043d\u0440, \u043a\u0430\u043a\u0442\u043e \u0438 **confusion matrix** \u0437\u0430 \u043d\u0430\u0439-\u0447\u0435\u0441\u0442\u043e \u0441\u0440\u0435\u0449\u0430\u043d\u0438\u0442\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0437\u0432\u043e\u043b\u044f\u0432\u0430 \u0430\u043d\u0430\u043b\u0438\u0437 \u043d\u0430 \u0442\u0438\u043f\u0438\u0447\u043d\u0438\u0442\u0435 \u0433\u0440\u0435\u0448\u043a\u0438 \u0438 \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435.\n"
# ### Оценка на моделите
#
# За оценка на класификационните модели е дефинирана обща функция, която извършва обучение, предсказване и изчисляване на основните метрики за качество.  
# Използват се **Accuracy** и **Macro F1**, като Macro F1 е водещата метрика поради многокласовия характер на задачата.
#
# Функцията извежда и **classification report** с Precision, Recall и F1-score за всеки жанр, както и **confusion matrix** за най-често срещаните жанрове, което позволява анализ на типичните грешки и припокривания между класовете.
#

# %% cell_id="0b66e4b3545a4d55b451f9c7284d796b" deepnote_block_group="af246d9e01ce4576b42f8c9385fdfa74" deepnote_cell_type="code" deepnote_content_hash="b844fba7" deepnote_execution_finished_at="2026-01-27T21:47:44.431Z" deepnote_execution_started_at="2026-01-27T21:47:44.431Z" deepnote_sorting_key="56" deepnote_source="def evaluate_classifier(\n    model_pipeline: Pipeline,\n    X_train,\n    y_train,\n    X_test,\n    y_test,\n    top_n: int = 10,\n    show_confusion: bool = True,\n    print_report: bool = True\n):\n    # \u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u0438 \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0432\u0430\u043d\u0435\n    model_pipeline.fit(X_train, y_train)\n    y_pred = model_pipeline.predict(X_test)\n\n    # \u041e\u0441\u043d\u043e\u0432\u043d\u0438 \u043c\u0435\u0442\u0440\u0438\u043a\u0438 - \u0438\u0437\u0431\u0440\u0430\u043b\u0438 \u0441\u043c\u0435 accuracy \u0438 macro f1\n    acc = accuracy_score(y_test, y_pred)\n    macro_f1 = f1_score(y_test, y_pred, average=\"macro\")\n\n    print(f\"Accuracy: {acc:.4f}\")\n    print(f\"Macro F1: {macro_f1:.4f}\")\n\n    # Classification report (precision/recall/F1 \u043f\u043e \u043a\u043b\u0430\u0441 + macro/weighted)\n    if print_report:\n        print(\"\\nClassification report:\")\n        print(classification_report(y_test, y_pred))\n\n    # Confusion matrix \u0437\u0430 top-N \u0436\u0430\u043d\u0440\u0430\n    if show_confusion:\n        top_genres = y_test.value_counts().head(top_n).index\n\n        mask = y_test.isin(top_genres)\n        y_test_top = y_test[mask]\n\n        y_pred_series = pd.Series(y_pred, index=y_test.index)\n        y_pred_top = y_pred_series[mask]\n\n        cm = confusion_matrix(y_test_top, y_pred_top, labels=top_genres)\n\n        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=top_genres)\n        plt.figure(figsize=(10, 8))\n        disp.plot(include_values=True, xticks_rotation=45)\n        plt.title(f\"Confusion Matrix (Top {top_n} \u0436\u0430\u043d\u0440\u0430)\")\n        plt.tight_layout()\n        plt.show()\n\n    return {\n        \"accuracy\": acc,\n        \"macro_f1\": macro_f1\n    }" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=0 execution_start=1769550464431 source_hash="b844fba7"
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


# %% [markdown] cell_id="010ef125255b412cb15224c1573d852c" deepnote_block_group="8c6ba168c01b4a839774487be8fde965" deepnote_cell_type="markdown" deepnote_sorting_key="57" deepnote_source="### Logistic Regression (baseline)\n\n\u041b\u0438\u043d\u0435\u0435\u043d \u043c\u043e\u0434\u0435\u043b, \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d \u043a\u0430\u0442\u043e \u0431\u0430\u0437\u0430 \u0437\u0430 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435. \u041f\u043e\u0434\u0445\u043e\u0434\u044f\u0449 \u0437\u0430 \u0431\u044a\u0440\u0437\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u043d\u0430 \u0442\u043e\u0432\u0430\n\u0434\u043e\u043a\u043e\u043b\u043a\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u0441\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u0438 \u0432 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e\u0442\u043e \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435.\n"
# ### Logistic Regression (baseline)
#
# Линеен модел, използван като база за сравнение. Подходящ за бърза оценка на това
# доколко жанровете са линейно разделими в пространството на признаците.
#

# %% cell_id="d4d24f3f3a944ae9869f9cfdc2c0fbac" deepnote_block_group="b0efb22a5f024bfdaf6ebe35cc45491a" deepnote_cell_type="code" deepnote_content_hash="9d2705f5" deepnote_execution_finished_at="2026-01-27T20:37:14.098Z" deepnote_execution_started_at="2026-01-27T20:35:56.161Z" deepnote_sorting_key="58" deepnote_source="logreg_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", LogisticRegression(max_iter=3000))\n])\n\nlogreg_results = evaluate_classifier(\n    model_pipeline=logreg_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=True,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=77937 execution_start=1769546156161 source_hash="9d2705f5"
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

# %% [markdown] cell_id="3fff7fe97b2d4d6d90f192ad3cf2b76d" deepnote_block_group="f3365c1a3cf54d4fa137fa3031ae9895" deepnote_cell_type="markdown" deepnote_sorting_key="59" deepnote_source="### k-Nearest Neighbors (kNN)\n\nkNN \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u0446\u0438\u0440\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u043d\u0430 \u0431\u0430\u0437\u0430 \u0441\u0445\u043e\u0434\u0441\u0442\u0432\u043e\u0442\u043e \u0438\u043c \u0441 \u043d\u0430\u0439-\u0431\u043b\u0438\u0437\u043a\u0438\u0442\u0435 \u043f\u0440\u0438\u043c\u0435\u0440\u0438 \u0432 feature \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e\u0442\u043e.\n\u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0435 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a\u044a\u043c \u043c\u0430\u0449\u0430\u0431\u0430 \u043d\u0430 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435, \u043f\u043e\u0440\u0430\u0434\u0438 \u043a\u043e\u0435\u0442\u043e \u043d\u043e\u0440\u043c\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u0435 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u0430.\n"
# ### k-Nearest Neighbors (kNN)
#
# kNN класифицира песните на база сходството им с най-близките примери в feature пространството.
# Моделът е чувствителен към мащаба на признаците, поради което нормализацията е необходима.
#

# %% cell_id="e9425d3c19e24517807c7cdeb713b03e" deepnote_block_group="7c973ad9c1d7434abe8c4f5f1efc0bb7" deepnote_cell_type="code" deepnote_content_hash="a4571e0f" deepnote_execution_finished_at="2026-01-27T20:39:25.099Z" deepnote_execution_started_at="2026-01-27T20:38:36.271Z" deepnote_sorting_key="60" deepnote_source="knn_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", KNeighborsClassifier(n_neighbors=15))\n])\n\nknn_results = evaluate_classifier(\n    model_pipeline=knn_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=48828 execution_start=1769546316271 source_hash="a4571e0f"
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

# %% [markdown] cell_id="830e41d2b0da422abecd892cfd7a010e" deepnote_block_group="2af4bc24623a45bb85a2fcf85d198a74" deepnote_cell_type="markdown" deepnote_sorting_key="61" deepnote_source="#### \u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u043d\u0430 kNN\n\n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 GridSearchCV \u0437\u0430 \u0438\u0437\u0431\u043e\u0440 \u043d\u0430 \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u0435\u043d \u0431\u0440\u043e\u0439 \u0441\u044a\u0441\u0435\u0434\u0438 \u0438 \u043d\u0430\u0447\u0438\u043d \u043d\u0430 \u043f\u0440\u0435\u0442\u0435\u0433\u043b\u044f\u043d\u0435,\n\u043a\u0430\u0442\u043e \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u0437\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u0435 Macro F1.\n"
# #### Настройка на хиперпараметрите на kNN
#
# Използва се GridSearchCV за избор на оптимален брой съседи и начин на претегляне,
# като критерий за оптимизация е Macro F1.
#

# %% cell_id="b76520ff91ac4c268a00c8f032efe6f9" deepnote_block_group="9b24bfe2efa944c8aae21ebc7317c000" deepnote_cell_type="code" deepnote_content_hash="344160ca" deepnote_execution_finished_at="2026-01-27T20:46:02.801Z" deepnote_execution_started_at="2026-01-27T20:39:25.191Z" deepnote_sorting_key="62" deepnote_source="knn_grid = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", KNeighborsClassifier())\n])\n\nparam_grid_knn = {\n    \"model__n_neighbors\": [5, 11, 21],\n    \"model__weights\": [\"uniform\", \"distance\"]\n}\n\ngs_knn = GridSearchCV(\n    estimator=knn_grid,\n    param_grid=param_grid_knn,\n    scoring=\"f1_macro\",\n    cv=3,\n    n_jobs=-1,\n    verbose=1\n)\n\ngs_knn.fit(X_train, y_train)\nprint(\"Best kNN params:\", gs_knn.best_params_)\n\nbest_knn = gs_knn.best_estimator_\n\nbest_knn_results = evaluate_classifier(\n    model_pipeline=best_knn,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=397610 execution_start=1769546365191 source_hash="344160ca"
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

# %% [markdown] cell_id="5dc7d76e7e9b4ece9c4fb801dd549bfd" deepnote_block_group="b9fe4444252741109718df9fe4c05d47" deepnote_cell_type="markdown" deepnote_sorting_key="63" deepnote_source="### Support Vector Machine (SVM)\n\n\u0418\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u0441\u0435 \u043b\u0438\u043d\u0435\u0439\u043d\u0430 SVM \u0432\u0435\u0440\u0441\u0438\u044f (`LinearSVC`), \u043a\u043e\u044f\u0442\u043e \u0435 \u043f\u043e-\u043f\u043e\u0434\u0445\u043e\u0434\u044f\u0449\u0430 \u0437\u0430 \u0433\u043e\u043b\u0435\u043c\u0438 \u043d\u0430\u0431\u043e\u0440\u0438 \u043e\u0442 \u0434\u0430\u043d\u043d\u0438\n\u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u043d\u0430 CPU. \u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0442\u044a\u0440\u0441\u0438 \u043e\u043f\u0442\u0438\u043c\u0430\u043b\u043d\u0430 \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u0449\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u043b\u043e\u0441\u043a\u043e\u0441\u0442 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n"
# ### Support Vector Machine (SVM)
#
# Използва се линейна SVM версия (`LinearSVC`), която е по-подходяща за големи набори от данни
# и работа на CPU. Моделът търси оптимална разделяща хиперплоскост между жанровете.
#

# %% cell_id="0550b953e8af4d7bb50b86f14fd6ef8f" deepnote_block_group="ba60de93f2144a1288bd803f7905fbfb" deepnote_cell_type="code" deepnote_content_hash="63fb9e22" deepnote_execution_finished_at="2026-01-27T21:09:15.284Z" deepnote_execution_started_at="2026-01-27T20:46:02.861Z" deepnote_sorting_key="64" deepnote_source="svm_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", LinearSVC())\n])\n\nsvm_results = evaluate_classifier(\n    model_pipeline=svm_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="0ae8260d-c38b-4184-a2d7-2829abbcd877" execution_millis=1392423 execution_start=1769546762861 source_hash="63fb9e22"
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

# %% [markdown] cell_id="5b17dedf350342288645f49a45f8c3b7" deepnote_block_group="e53271f9a40a45cdb0d6af89a0970abd" deepnote_cell_type="markdown" deepnote_sorting_key="65" deepnote_source="### Decision Tree \u0438 Random Forest\n\n\u0414\u044a\u0440\u0432\u0435\u0442\u0430\u0442\u0430 \u0437\u0430 \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430\u0442 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435.\nRandom Forest \u043a\u043e\u043c\u0431\u0438\u043d\u0438\u0440\u0430 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430 \u0438 \u043e\u0431\u0438\u043a\u043d\u043e\u0432\u0435\u043d\u043e \u0434\u0430\u0432\u0430 \u043f\u043e-\u0441\u0442\u0430\u0431\u0438\u043b\u043d\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\n\u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u0435\u0434\u0438\u043d\u0438\u0447\u043d\u043e \u0434\u044a\u0440\u0432\u043e.\n"
# ### Decision Tree и Random Forest
#
# Дърветата за решения могат да моделират нелинейни зависимости между признаците.
# Random Forest комбинира множество дървета и обикновено дава по-стабилни резултати
# в сравнение с единично дърво.
#

# %% cell_id="9bba37da27d44d4183dbed5cb8a6f11c" deepnote_block_group="0cdec216345240e2b8f4f45d7c27b9bd" deepnote_cell_type="code" deepnote_content_hash="8ae79cdc" deepnote_execution_finished_at="2026-01-27T21:47:58.689Z" deepnote_execution_started_at="2026-01-27T21:47:55.526Z" deepnote_sorting_key="66" deepnote_source="dt_model = Pipeline(steps=[\n    (\"prep\", \"passthrough\"),\n    (\"model\", DecisionTreeClassifier(\n        random_state=42,\n        max_depth=20,\n        min_samples_leaf=5\n    ))\n])\n\ndt_results = evaluate_classifier(\n    model_pipeline=dt_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=3163 execution_start=1769550475526 source_hash="8ae79cdc"
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

# %% cell_id="b0f468d48afc4d3e99e90810e8c0108e" deepnote_block_group="65013a9a68dc48b0927473786352a126" deepnote_cell_type="code" deepnote_content_hash="f6df638e" deepnote_execution_finished_at="2026-01-27T21:48:38.014Z" deepnote_execution_started_at="2026-01-27T21:48:04.280Z" deepnote_sorting_key="67" deepnote_source="rf_model = Pipeline(steps=[\n    (\"prep\", \"passthrough\"),\n    (\"model\", RandomForestClassifier(\n        n_estimators=80,\n        max_depth=20,\n        min_samples_leaf=3,\n        random_state=42,\n        n_jobs=1\n    ))\n])\n\nrf_results = evaluate_classifier(\n    model_pipeline=rf_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=True,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=33734 execution_start=1769550484280 source_hash="f6df638e"
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

# %% [markdown] cell_id="ba6f4cba130344959ea3f714d456c850" deepnote_block_group="5b29c57ea3a64cb98ba7376553b8eb10" deepnote_cell_type="markdown" deepnote_sorting_key="68" deepnote_source="### MLPClassifier\n\nMLPClassifier \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u044f\u0432\u0430 \u043c\u043d\u043e\u0433\u043e\u0441\u043b\u043e\u0435\u043d \u043f\u0435\u0440\u0446\u0435\u043f\u0442\u0440\u043e\u043d, \u043a\u043e\u0439\u0442\u043e \u043c\u043e\u0436\u0435 \u0434\u0430 \u0443\u043b\u0430\u0432\u044f \u0441\u043b\u043e\u0436\u043d\u0438 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\u041c\u043e\u0434\u0435\u043b\u044a\u0442 \u0441\u043b\u0443\u0436\u0438 \u043a\u0430\u0442\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u043f\u043e\u0434\u0445\u043e\u0434 \u043e\u0442 \u0443\u0447\u0435\u0431\u043d\u0438\u044f \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b.\n"
# ### MLPClassifier
#
# MLPClassifier представлява многослоен перцептрон, който може да улавя сложни нелинейни зависимости.
# Моделът служи като допълнителен сравнителен подход от учебния материал.
#

# %% cell_id="7299629268de410692c2f0c504927502" deepnote_block_group="7c5b5878829644428b468b9f2d30cb91" deepnote_cell_type="code" deepnote_content_hash="5c560f01" deepnote_execution_finished_at="2026-01-27T21:59:48.094Z" deepnote_execution_started_at="2026-01-27T21:48:38.071Z" deepnote_sorting_key="69" deepnote_source="mlp_model = Pipeline(steps=[\n    (\"prep\", preprocess_cls),\n    (\"model\", MLPClassifier(\n        hidden_layer_sizes=(64, 32),\n        activation=\"relu\",\n        solver=\"adam\",\n        max_iter=60,\n        batch_size=512,\n        early_stopping=True,\n        validation_fraction=0.1,\n        n_iter_no_change=8,\n        random_state=42\n    ))\n])\n\nmlp_results = evaluate_classifier(\n    model_pipeline=mlp_model,\n    X_train=X_train, y_train=y_train,\n    X_test=X_test, y_test=y_test,\n    top_n=10,\n    show_confusion=False,\n    print_report=False\n)" execution_context_id="17dd6f18-cfe3-4722-a34d-95bf1ec627aa" execution_millis=670023 execution_start=1769550518071 source_hash="5c560f01"
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

# %% [markdown] cell_id="dea4ec7c106c415fa60dd2ecb59649d8" deepnote_block_group="d548225f8cd240858064b96413bb0c29" deepnote_cell_type="markdown" deepnote_sorting_key="70" deepnote_source="## \u0418\u043d\u0442\u0435\u0440\u043f\u0440\u0435\u0442\u0430\u0446\u0438\u044f \u043d\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 (\u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f \u043d\u0430 \u0436\u0430\u043d\u0440)\n\n### \u041e\u0431\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043d\u0430 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435\u0442\u043e\n\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0442\u0435 \u043c\u043e\u0434\u0435\u043b\u0438 \u043f\u043e\u043a\u0430\u0437\u0432\u0430\u0442, \u0447\u0435 \u0437\u0430\u0434\u0430\u0447\u0430\u0442\u0430 \u0435 \u0442\u0440\u0443\u0434\u043d\u0430 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u043d\u0430 \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435, \u043d\u043e \u0432\u0441\u0435 \u043f\u0430\u043a \u0438\u043c\u0430 \u044f\u0441\u043d\u0438 \u0440\u0430\u0437\u043b\u0438\u043a\u0438 \u043c\u0435\u0436\u0434\u0443 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438\u0442\u0435:\n\n- **Logistic Regression**: Accuracy = 0.1984, Macro F1 = 0.1694  \n  \u041b\u0438\u043d\u0435\u0435\u043d \u0431\u0430\u0437\u043e\u0432 \u043c\u043e\u0434\u0435\u043b. \u0414\u0430\u0432\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u043d\u043e \u043d\u0438\u0441\u043a\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435 \u043d\u0435 \u0441\u0430 \u0434\u043e\u0431\u0440\u0435 \u043b\u0438\u043d\u0435\u0439\u043d\u043e \u0440\u0430\u0437\u0434\u0435\u043b\u0438\u043c\u0438 \u0441\u0430\u043c\u043e \u043f\u043e \u0442\u0435\u0437\u0438 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438.\n\n- **kNN**: Accuracy = 0.2137, Macro F1 = 0.2042  \n  \u041f\u043e\u0434\u043e\u0431\u0440\u044f\u0432\u0430 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0441\u043f\u0440\u044f\u043c\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u0438\u044f baseline, \u043a\u043e\u0435\u0442\u043e \u0435 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e, \u0437\u0430\u0449\u043e\u0442\u043e \u043c\u0435\u0442\u043e\u0434\u044a\u0442 \u0443\u043b\u0430\u0432\u044f \u043b\u043e\u043a\u0430\u043b\u043d\u0438 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\n- **kNN + GridSearch**: Accuracy = 0.2207, Macro F1 = 0.2158  \n  \u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 (k=21, weights=distance) \u0432\u043e\u0434\u0438 \u0434\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e (\u0443\u043c\u0435\u0440\u0435\u043d\u043e) \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0435 \u2014 \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430\u0442\u0430 \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435 \u0438\u043c\u0430 \u0440\u0435\u0430\u043b\u0435\u043d \u0435\u0444\u0435\u043a\u0442.\n\n- **SVM (LinearSVC)**: Accuracy = 0.1723, Macro F1 = 0.1111  \n  \u041d\u0430\u0439-\u0441\u043b\u0430\u0431\u0438\u044f\u0442 \u043c\u043e\u0434\u0435\u043b \u0432 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441 \u043e\u0441\u0442\u0430\u043d\u0430\u043b\u0438\u0442\u0435. ConvergenceWarning \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f\u0442\u0430 \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0438\u0433\u043d\u0430\u043b\u0430 \u0441\u0442\u0430\u0431\u0438\u043b\u043d\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u0437\u0430\u0434\u0430\u0434\u0435\u043d\u0438\u0442\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0438, \u0430 \u043e\u0441\u0432\u0435\u043d \u0442\u043e\u0432\u0430 \u043b\u0438\u043d\u0435\u0439\u043d\u0430\u0442\u0430 \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u0430 \u0437\u0430 \u0434\u043e\u0431\u0440\u0435 \u0440\u0430\u0437\u0434\u0435\u043b\u044f\u043d\u0435 \u043d\u0430 \u0436\u0430\u043d\u0440\u043e\u0432\u0435\u0442\u0435.\n\n- **Decision Tree**: Accuracy = 0.2302, Macro F1 = 0.2314  \n  \u041f\u043e-\u0434\u043e\u0431\u0440\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0435 \u043e\u0442 \u043b\u0438\u043d\u0435\u0439\u043d\u0438\u0442\u0435 \u043f\u043e\u0434\u0445\u043e\u0434\u0438. \u0414\u044a\u0440\u0432\u043e\u0442\u043e \u043c\u043e\u0436\u0435 \u0434\u0430 \u0443\u043b\u0430\u0432\u044f \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u043a\u0430\u0442\u043e \u0435\u0434\u0438\u043d\u0438\u0447\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u0435 \u043f\u043e-\u043d\u0435\u0441\u0442\u0430\u0431\u0438\u043b\u043d\u043e \u0438 \u043b\u0435\u0441\u043d\u043e \u043d\u0430\u0443\u0447\u0430\u0432\u0430 \u0448\u0443\u043c/\u0441\u043f\u0435\u0446\u0438\u0444\u0438\u0447\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438.\n\n- **Random Forest**: Accuracy = 0.3205, Macro F1 = 0.3112  \n  \u041d\u0430\u0439-\u0434\u043e\u0431\u0440\u0438\u044f\u0442 \u043c\u043e\u0434\u0435\u043b. \u041a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u044f\u0442\u0430 \u043e\u0442 \u043c\u043d\u043e\u0433\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430 \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f\u0442\u0430 \u0438 \u0443\u043b\u0430\u0432\u044f \u043f\u043e-\u0441\u043b\u043e\u0436\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435, \u043a\u043e\u0435\u0442\u043e \u0432\u043e\u0434\u0438 \u0434\u043e \u043e\u0441\u0435\u0437\u0430\u0435\u043c\u043e \u043f\u043e-\u0434\u043e\u0431\u0440\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438.\n\n- **MLPClassifier**: Accuracy = 0.2865, Macro F1 = 0.2651  \n  \u0421\u0438\u043b\u0435\u043d \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442, \u043d\u043e \u043f\u043e\u0434 Random Forest. ConvergenceWarning \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u043f\u0440\u0438 \u043f\u043e\u0432\u0435\u0447\u0435 \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0438 (\u0438\u043b\u0438 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438) \u0435 \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u043e \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u043e \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u0435, \u043d\u043e \u0442\u043e\u0432\u0430 \u0442\u0440\u044f\u0431\u0432\u0430 \u0434\u0430 \u0441\u0435 \u0431\u0430\u043b\u0430\u043d\u0441\u0438\u0440\u0430 \u0441\u043f\u0440\u044f\u043c\u043e \u0432\u0440\u0435\u043c\u0435\u0442\u043e/\u0440\u0435\u0441\u0443\u0440\u0441\u0438\u0442\u0435 \u0432 \u0441\u0440\u0435\u0434\u0430\u0442\u0430.\n\n**\u0414\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0430 \u0431\u0435\u043b\u0435\u0436\u043a\u0430:** Confusion matrix \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u043f\u043e\u0447\u0442\u0438 \u043f\u0440\u0430\u0437\u043d\u0430 (\u0447\u0435\u0440\u043d\u0430 \u0438\u0437\u0432\u044a\u043d \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0430). \u041f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u043a\u043b\u0430\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f (\u0432 \u0441\u043b\u0443\u0447\u0430\u044f \u0438\u043c\u0430\u043c\u0435 \u043c\u043d\u043e\u0433\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435) \u0433\u0440\u0435\u0448\u043a\u0438\u0442\u0435 \u0441\u0435 \u0440\u0430\u0437\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0442 \u043c\u0435\u0436\u0434\u0443 \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u0434\u0440\u0443\u0433\u0438 \u043a\u043b\u0430\u0441\u043e\u0432\u0435 \u0438 \u043f\u043e\u0432\u0435\u0447\u0435\u0442\u043e \u043a\u043b\u0435\u0442\u043a\u0438 \u0438\u0437\u0432\u044a\u043d \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0430 \u0438\u043c\u0430\u0442 \u043c\u043d\u043e\u0433\u043e \u043c\u0430\u043b\u043a\u0438 \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438 (\u0447\u0435\u0441\u0442\u043e 0\u20132). \u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043c\u0435 Top-N (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 10) \u0436\u0430\u043d\u0440\u0430, \u043a\u043e\u0435\u0442\u043e \u043f\u0440\u0430\u0432\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u0430\u0442\u0430 \u0447\u0435\u0442\u0438\u043c\u0430, \u043d\u043e \u0433\u0440\u0435\u0448\u043a\u0438\u0442\u0435 \u043d\u0430 \u043f\u0435\u0441\u043d\u0438\u0442\u0435 \u043e\u0442 \u0442\u0435\u0437\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0447\u0435\u0441\u0442\u043e \u0441\u0430 \u043a\u044a\u043c \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438\u0437\u0432\u044a\u043d Top-N. \u0412 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0437\u0430 \u0432\u0441\u0438\u0447\u043a\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u043c\u0430\u0442\u0440\u0438\u0446\u0430\u0442\u0430 \u0438\u0437\u0433\u043b\u0435\u0436\u0434\u0430 \u0441\u0445\u043e\u0434\u043d\u043e: \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044a\u0442 \u0435 \u043d\u0430\u0439-\u0441\u0432\u0435\u0442\u044a\u043b, \u0430 \u0438\u0437\u0432\u044a\u043d \u043d\u0435\u0433\u043e \u0441\u0442\u043e\u0439\u043d\u043e\u0441\u0442\u0438\u0442\u0435 \u0441\u0430 \u0440\u0430\u0437\u043f\u0440\u044a\u0441\u043d\u0430\u0442\u0438 \u0438 \u0432\u0438\u0437\u0443\u0430\u043b\u043d\u043e \u043f\u043e\u0447\u0442\u0438 \u043d\u0435 \u0441\u0435 \u043e\u0442\u043b\u0438\u0447\u0430\u0432\u0430\u0442.\n\n### \u0417\u0430\u0449\u043e \u043d\u044f\u043a\u043e\u0438 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438 \u0441\u0435 \u0441\u043f\u0440\u0430\u0432\u044f\u0442 \u043f\u043e-\u0434\u043e\u0431\u0440\u0435 \u043e\u0442 \u0434\u0440\u0443\u0433\u0438\n\n\u0420\u0430\u0437\u043b\u0438\u043a\u0438\u0442\u0435 \u0432 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438\u0442\u0435 \u0438\u0434\u0432\u0430\u0442 \u043e\u0441\u043d\u043e\u0432\u043d\u043e \u043e\u0442 \u0442\u043e\u0432\u0430 \u043a\u0430\u043a \u043c\u043e\u0434\u0435\u043b\u0438\u0442\u0435 \u043c\u043e\u0433\u0430\u0442 \u0434\u0430 \u043e\u043f\u0438\u0441\u0432\u0430\u0442 \u0432\u0440\u044a\u0437\u043a\u0430\u0442\u0430 \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 \u0438 \u0436\u0430\u043d\u0440\u0430. \u041b\u0438\u043d\u0435\u0439\u043d\u0438\u044f\u0442 baseline (Logistic Regression) \u0438\u043c\u0430 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0435 \u0434\u0430 \u043d\u0430\u043c\u0438\u0440\u0430 \u0441\u0430\u043c\u043e \u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0433\u0440\u0430\u043d\u0438\u0446\u0438 \u043c\u0435\u0436\u0434\u0443 \u043a\u043b\u0430\u0441\u043e\u0432\u0435\u0442\u0435, \u0430 \u043f\u0440\u0438 \u043c\u043d\u043e\u0433\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0431\u043b\u0438\u0437\u043a\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u0438 \u0442\u043e\u0432\u0430 \u0447\u0435\u0441\u0442\u043e \u043d\u0435 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u043e. kNN \u0441\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f \u043f\u043e-\u0434\u043e\u0431\u0440\u0435, \u0437\u0430\u0449\u043e\u0442\u043e \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430 \u043b\u043e\u043a\u0430\u043b\u043d\u043e \u0441\u0445\u043e\u0434\u0441\u0442\u0432\u043e \u0438 \u0443\u043b\u0430\u0432\u044f \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u0435 \u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d \u043a\u044a\u043c \u0448\u0443\u043c \u0438 \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u043d\u0435 \u043c\u0435\u0436\u0434\u0443 \u0436\u0430\u043d\u0440\u043e\u0432\u0435. Decision Tree \u043c\u043e\u0436\u0435 \u0434\u0430 \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0441\u0442\u0438, \u043d\u043e \u043a\u0430\u0442\u043e \u0435\u0434\u0438\u043d\u0438\u0447\u0435\u043d \u043c\u043e\u0434\u0435\u043b \u0435 \u043d\u0435\u0441\u0442\u0430\u0431\u0438\u043b\u0435\u043d \u0438 \u0441\u043a\u043b\u043e\u043d\u0435\u043d \u043a\u044a\u043c overfitting. Random Forest \u0434\u0430\u0432\u0430 \u043d\u0430\u0439-\u0434\u043e\u0431\u0440\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u0437\u0430\u0449\u043e\u0442\u043e \u0443\u0441\u0440\u0435\u0434\u043d\u044f\u0432\u0430 \u043c\u043d\u043e\u0433\u043e \u0434\u044a\u0440\u0432\u0435\u0442\u0430, \u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430 \u0434\u0438\u0441\u043f\u0435\u0440\u0441\u0438\u044f\u0442\u0430 \u0438 \u0443\u043b\u0430\u0432\u044f \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435 (\u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u043a\u043e\u043c\u0431\u0438\u043d\u0430\u0446\u0438\u0438), \u043a\u043e\u0435\u0442\u043e \u0435 \u0432\u0430\u0436\u043d\u043e \u0437\u0430 \u0441\u043b\u043e\u0436\u043d\u0430 \u043c\u043d\u043e\u0433\u043e\u043a\u043b\u0430\u0441\u043e\u0432\u0430 \u0437\u0430\u0434\u0430\u0447\u0430 \u043a\u0430\u0442\u043e \u0442\u0430\u0437\u0438. MLP \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u0432\u0438\u0441\u043e\u043a\u0438 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442\u0438, \u0442\u044a\u0439 \u043a\u0430\u0442\u043e \u0441\u044a\u0449\u043e \u043c\u043e\u0434\u0435\u043b\u0438\u0440\u0430 \u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438, \u043d\u043e \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435\u0442\u043e \u043c\u0443 \u0435 \u043f\u043e-\u0442\u0440\u0443\u0434\u043d\u043e \u0437\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u043c\u043e\u0436\u0435 \u0434\u0430 \u043d\u0435 \u043a\u043e\u043d\u0432\u0435\u0440\u0433\u0438\u0440\u0430 \u043d\u0430\u043f\u044a\u043b\u043d\u043e \u043f\u0440\u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438 \u0440\u0435\u0441\u0443\u0440\u0441\u0438.\n\n### \u0417\u0430\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u0438 \u0432\u044a\u0437\u043c\u043e\u0436\u043d\u0438 \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f\n\n\u041d\u0430\u0439-\u0434\u043e\u0431\u044a\u0440 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0432 \u0435\u043a\u0441\u043f\u0435\u0440\u0438\u043c\u0435\u043d\u0442\u0438\u0442\u0435 \u043f\u043e\u043a\u0430\u0437\u0432\u0430 Random Forest, \u043d\u043e \u0434\u043e\u0440\u0438 \u0442\u043e\u0439 \u043d\u0435 \u043f\u043e\u0441\u0442\u0438\u0433\u0430 \u043c\u043d\u043e\u0433\u043e \u0432\u0438\u0441\u043e\u043a\u0430 \u0442\u043e\u0447\u043d\u043e\u0441\u0442, \u043a\u043e\u0435\u0442\u043e \u0435 \u043e\u0447\u0430\u043a\u0432\u0430\u043d\u043e \u043f\u0440\u0438 \u0433\u043e\u043b\u044f\u043c \u0431\u0440\u043e\u0439 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 \u0438 \u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u043f\u0440\u0438\u043f\u043e\u043a\u0440\u0438\u0432\u0430\u0449\u0438 \u0441\u0435 \u0430\u0443\u0434\u0438\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438. \u0421\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u043d\u043e \u043c\u043e\u0434\u0435\u043b\u044a\u0442 \u0435 \u0434\u043e\u0441\u0442\u0430\u0442\u044a\u0447\u043d\u043e \u0434\u043e\u0431\u044a\u0440 \u0437\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u043e\u0434\u0445\u043e\u0434\u0430 \u0438 \u0437\u0430 \u0441\u0440\u0430\u0432\u043d\u0438\u0442\u0435\u043b\u0435\u043d \u0430\u043d\u0430\u043b\u0438\u0437 \u043c\u0435\u0436\u0434\u0443 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0438, \u043d\u043e \u043d\u0435 \u0435 \u201c\u043f\u0435\u0440\u0444\u0435\u043a\u0442\u043d\u043e\u201d \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0437\u0430 \u043d\u0430\u0434\u0435\u0436\u0434\u043d\u043e \u0436\u0430\u043d\u0440\u043e\u0432\u043e \u0440\u0430\u0437\u043f\u043e\u0437\u043d\u0430\u0432\u0430\u043d\u0435. \u041f\u043e\u0442\u0435\u043d\u0446\u0438\u0430\u043b\u043d\u0438 \u043f\u043e\u0434\u043e\u0431\u0440\u0435\u043d\u0438\u044f \u0441\u0430: \u043f\u043e-\u0437\u0430\u0434\u044a\u043b\u0431\u043e\u0447\u0435\u043d\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u043d\u0430 \u0445\u0438\u043f\u0435\u0440\u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438 (\u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u043e \u0441\u043f\u0440\u044f\u043c\u043e \u0440\u0435\u0441\u0443\u0440\u0441\u0438\u0442\u0435), \u0434\u043e\u0431\u0430\u0432\u044f\u043d\u0435 \u043d\u0430 \u0434\u043e\u043f\u044a\u043b\u043d\u0438\u0442\u0435\u043b\u043d\u0438 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 (\u043d\u0430\u043f\u0440. \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0438 \u0434\u0430\u043d\u043d\u0438 \u0438\u043b\u0438 \u043f\u043e-\u0431\u043e\u0433\u0430\u0442\u0438 \u0430\u0443\u0434\u0438\u043e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u044f\u043d\u0438\u044f), \u043e\u0431\u0435\u0434\u0438\u043d\u044f\u0432\u0430\u043d\u0435/\u0439\u0435\u0440\u0430\u0440\u0445\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u0441\u0445\u043e\u0434\u043d\u0438 \u0436\u0430\u043d\u0440\u043e\u0432\u0435 (\u043d\u0430\u043c\u0430\u043b\u044f\u0432\u0430\u043d\u0435 \u043d\u0430 \u0431\u0440\u043e\u044f \u043a\u043b\u0430\u0441\u043e\u0432\u0435), \u0438 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d\u0435 \u043d\u0430 \u043f\u043e-\u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0438\u0440\u0430\u043d\u0438 \u043c\u043e\u0434\u0435\u043b\u0438 \u0437\u0430 \u0430\u0443\u0434\u0438\u043e (\u043d\u0430\u043f\u0440. \u043c\u043e\u0434\u0435\u043b\u0438 \u0432\u044a\u0440\u0445\u0443 \u0441\u043f\u0435\u043a\u0442\u0440\u043e\u0433\u0440\u0430\u043c\u0438 \u0438\u043b\u0438 embedding-\u0438).\n\n\n### \u0418\u0437\u0432\u043e\u0434 \u043e\u0442 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f\u0442\u0430\n\u041d\u0430\u0439-\u0434\u043e\u0431\u044a\u0440 \u0440\u0435\u0437\u0443\u043b\u0442\u0430\u0442 \u0434\u0430\u0432\u0430 **Random Forest**, \u043a\u043e\u0435\u0442\u043e \u043f\u043e\u043a\u0430\u0437\u0432\u0430, \u0447\u0435 \u0437\u0430 \u0442\u0435\u0437\u0438 \u0434\u0430\u043d\u043d\u0438 \u0441\u0430 \u0432\u0430\u0436\u043d\u0438 **\u043d\u0435\u043b\u0438\u043d\u0435\u0439\u043d\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0438 \u0432\u0437\u0430\u0438\u043c\u043e\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u0440\u0438\u0437\u043d\u0430\u0446\u0438\u0442\u0435**. \u0421\u043b\u0435\u0434\u0432\u0430\u0449\u0438\u044f\u0442 \u043b\u043e\u0433\u0438\u0447\u0435\u043d \u0438\u0437\u0431\u043e\u0440 \u0435 \u0442\u043e\u0437\u0438 \u043c\u043e\u0434\u0435\u043b \u0434\u0430 \u0431\u044a\u0434\u0435 \u0438\u0437\u043f\u043e\u043b\u0437\u0432\u0430\u043d \u043a\u0430\u0442\u043e \u043e\u0441\u043d\u043e\u0432\u0435\u043d \u0437\u0430 \u0444\u0438\u043d\u0430\u043b\u043d\u0430\u0442\u0430 \u043e\u0446\u0435\u043d\u043a\u0430 \u0438 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u044f \u043d\u0430 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0442\u0435.\n"
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

# %% [markdown]
# # Част 2. Кластъризация

# %% [markdown]
# ## Подготовка на данни за клъстеризация
#
# При клъстеризация целта е да се групират песни без предварително зададени етикети (unsupervised learning). Вместо да предсказваме жанр, търсим естествени групи в данните, базирани на сходство в аудио характеристиките.
#
# **Основни разлики спрямо класификацията:**
# - Няма целева променлива (`track_genre`)
# - Фокус върху аудио характеристики, свързани със звучене и настроение
# - Scaling е критичен, тъй като алгоритмите са distance-based (напр. K-Means, DBSCAN)
# - Не се прави train/test split (всички данни се използват за клъстеризация)

# %%
# Подготовка на данни за клъстеризация
df_clust = df.copy()

# Премахване на дубликати и редове с липсващи стойности
df_clust = df_clust.drop_duplicates()
df_clust = df_clust.dropna()

# Explicit към числова стойност
if "explicit" in df_clust.columns:
    df_clust["explicit"] = df_clust["explicit"].astype(int)

print(f"Размер на данните за клъстеризация: {df_clust.shape}")

# %%
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

# %%
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

# %%
# Проверка на статистики след scaling
print("Статистики след нормализация:")
print(X_clust_scaled_df.describe())

# %% [markdown]
# ### Optional: Намаляване на размерност с PCA
#
# За улеснение на визуализацията и евентуално ускоряване на алгоритмите можем да приложим PCA (Principal Component Analysis). Това намалява броя на признаците, като запазва най-важната информация.

# %%
# Прилагане на PCA (запазваме напр. 95% от вариацията)
pca = PCA(n_components=0.95, random_state=42)
X_clust_pca = pca.fit_transform(X_clust_scaled)

print(f"Оригинален брой признаци: {X_clust_scaled.shape[1]}")
print(f"Брой компоненти след PCA (95% variance): {pca.n_components_}")
print(f"Обяснена вариация по компоненти: {pca.explained_variance_ratio_}")
print(f"Обща обяснена вариация: {pca.explained_variance_ratio_.sum():.4f}")

# %%
X_clust_scaled_df.columns

# %%
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

# %% [markdown]
# От тази визуализация можем да разберем, че данните са комплексни и всички признаци са важни – дори най-слабо обяснителният компонент допринася около 5% от общата вариация. Това показва, че за постигане на 95% запазена вариация са необходими повечето от първоначалните характеристики, което подчертава сложността на музикалните данни.

# %% [markdown]
# ## Разделяне на клъстъри

# %%
from scipy.cluster.hierarchy import dendrogram, linkage

# %%
# Hierarchical clustering изисква много памет за пълния dataset
# Използваме стратифициран sample с еднакъв брой песни от всеки жанр
songs_per_genre = 375  # Еднакъв брой песни от всеки жанр
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

linked = linkage(X_sample, method='ward')

# %%
linked_complete = linkage(X_sample, method='complete')

# %%
linked_average = linkage(X_sample, method='average')

# %%
fig, axes = plt.subplots(1, 3, figsize=(18, 7))

dendrogram(linked, truncate_mode='level', p=8, ax=axes[0])
axes[0].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Ward Linkage)")
axes[0].axhline(y=90, color='r', linestyle='-')

dendrogram(linked_complete, truncate_mode='level', p=8, ax=axes[1])
axes[1].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Complete Linkage)")
axes[1].axhline(y=10.5, color='r', linestyle='-')

dendrogram(linked_average, truncate_mode='level', p=8, ax=axes[2])
axes[2].set_title("Hierarchical Clustering Dendrogram (Super-Genres) (Average Linkage)")
axes[2].axhline(y=6.2, color='r', linestyle='-')

plt.tight_layout()
plt.show()

# %%
import matplotlib.pyplot as plt
import numpy as np

last_number_of_distances = 110
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

# %% [markdown]
# С помощта на функцията linkage от scipy и метода на Ward генерирахме йерархия на клъстерите. За да определим оптималния брой клъстери (k), анализирахме дендрограмата, търсейки най-голямото вертикално разстояние (gap) между последователни обединявания. Голямата дължина на вертикалните линии при метода на Ward индикира значително нарастване на вътрешната вариация при обединяване, което математически подсказва, че клъстерите преди сливането са добре разграничени.
#
# На графиките се вижда, че k=2 или k=3 са математически най-обособените разделения. В нашия случай обаче те не са подходящи, тъй като целта е данните да се разделят на немалък брой клъстери, за да се улеснят моделите за класификация на второ ниво.
#
# Според резултатите от метода на лакътя (Elbow method), приложен върху дистанциите на Ward Linkage, се вижда, че след k=11 вече няма толкова значително намаление на цената (cost/distance). Основно ще вземем предвид резултатите от Ward Linkage, тъй като този метод е най-подходящ за нашите цели – стремим се към възможно най-плътни (dense) клъстери

# %%
k=7

# %% [markdown]
# ### Grid Search за оптимално k
#
# За да изберем най-добрия брой клъстери, ще изпълним grid search с различни метрики за оценка:
# - **Silhouette Score** - мери колко добре всеки обект пасва на своя клъстър (стойности от -1 до 1, по-високи са по-добри)
# - **Calinski-Harabasz Score** - съотношение на между-клъстерна и вътрешно-клъстерна дисперсия (по-високо е по-добре)
# - **Davies-Bouldin Score** - средна прилика между клъстери (по-ниско е по-добре)

# %%
import numpy as np
from sklearn.cluster import AgglomerativeClustering

model = AgglomerativeClustering(n_clusters=k, linkage='ward')
labels = model.fit_predict(X_sample)    

unique, counts = np.unique(labels, return_counts=True)
print(dict(zip(unique, counts)))

# %%
from sklearn.metrics import silhouette_score

score = silhouette_score(X_sample, labels)
print(f"Silhouette Score for k={k}: {score:.3f}")

# %%
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_sample, labels)

# %% [markdown]
# Заради проблема с изискването на голям обем RAM, трябва да измислим оптимизация. Планирам да направя клъстеринг само върху представителна извадка (sample) от данните. След това ще използвам KNN (K-Nearest Neighbors), за да класифицирам останалите данни към вече създадените клъстери. По този начин процесът на клъстериране ще се оптимизира значително

# %%
labels_full = knn.predict(X_clust_scaled)

# %%
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

k_range = [2, 5, 7, 11, 15, 20, 25, 30, 40, 50]

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

# %%
optimal_k = np.partition(k_range, -1)[-5:]
print(f"\nИзползване на оптималното k = {optimal_k} за финално клъстеризиране...")


# %%
def visualize_cluster_distribution(df_clust, labels_full, title="Разпределение на жанрове по клъстери"):    
    cluster_genre_df = pd.DataFrame({
        'cluster': labels_full,
        'genre': df_clust['track_genre'].values
    })
    
    contingency_table = pd.crosstab(cluster_genre_df['cluster'], 
                                    cluster_genre_df['genre'])
    
    top_genres = df_clust['track_genre'].value_counts().head(15).index
    contingency_table_top = contingency_table[top_genres]
    
    fig, axes = plt.subplots(2, 2, figsize=(20, 14))
    
    contingency_table_top.plot(kind='bar', stacked=True, ax=axes[0, 0], 
                               colormap='tab20', width=0.8)
    axes[0, 0].set_title('Разпределение на топ 15 жанра по клъстери (абсолютни стойности)', 
                        fontsize=14, fontweight='bold')
    axes[0, 0].set_xlabel('Клъстър', fontsize=12)
    axes[0, 0].set_ylabel('Брой песни', fontsize=12)
    axes[0, 0].legend(title='Жанр', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    contingency_table_top_pct = contingency_table_top.div(
        contingency_table_top.sum(axis=1), axis=0
    ) * 100
    contingency_table_top_pct.plot(kind='bar', stacked=True, ax=axes[0, 1], 
                                   colormap='tab20', width=0.8)
    axes[0, 1].set_title('Разпределение на топ 15 жанра по клъстери (проценти)', 
                        fontsize=14, fontweight='bold')
    axes[0, 1].set_xlabel('Клъстър', fontsize=12)
    axes[0, 1].set_ylabel('Процент (%)', fontsize=12)
    axes[0, 1].legend(title='Жанр', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    sns.heatmap(contingency_table_top.T, annot=True, fmt='d', cmap='YlOrRd', 
                ax=axes[1, 0], cbar_kws={'label': 'Брой песни'})
    axes[1, 0].set_title('Heatmap на топ 15 жанра по клъстери', 
                        fontsize=14, fontweight='bold')
    axes[1, 0].set_xlabel('Клъстър', fontsize=12)
    axes[1, 0].set_ylabel('Жанр', fontsize=12)
    
    cluster_sizes = pd.Series(labels_full).value_counts().sort_index()
    axes[1, 1].bar(cluster_sizes.index, cluster_sizes.values, 
                  color='steelblue', alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('Размер на клъстерите', fontsize=14, fontweight='bold')
    axes[1, 1].set_xlabel('Клъстър', fontsize=12)
    axes[1, 1].set_ylabel('Брой песни', fontsize=12)
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    for i, v in enumerate(cluster_sizes.values):
        axes[1, 1].text(cluster_sizes.index[i], v, str(v), 
                       ha='center', va='bottom', fontsize=10, fontweight='bold')
    
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
    
    return contingency_table


# %%
contingency_table = visualize_cluster_distribution(df_clust, labels_full)

# %% [markdown]
# Анализът показа, че изборът на 7 клъстера (k=7) е па-доброто стратегическо решение, защото k=11 не дава толково добър резултат. Алгоритъмът успешно разпозна седем отчетливи супер-жанра: Мейнстрийм/Парти, Атмосфера/Релакс, Тежка музика, Органична/Вокална, Комедия, Бразилски ритми и Технична електроника. Този избор запази важни малки групи като Комедия и Музика за сън, които щяха да се загубят при друг брой клъстери. Единственият недостатък е, че Клъстър 0 (Мейнстрийм) остана твърде голям с 39 000 песни. Затова следващата стъпка е йерархична под-клъстеризация: ще запазим текущия модел като първо ниво, но ще изолираме само Клъстър 0 и ще приложим алгоритъма повторно само върху него. Това ще позволи да разделим огромната група на по-точни под-жанрове, без да разваляме структурата на останалите добре обособени групи.
