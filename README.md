# fedsfm_data

Gather & visualize data from fedsfm terrorists and extremists list.

## stack

python 3.7, pipenv, plotly

## how to install

```bash
$ pipenv install
```

## how to run

```bash
$ pipenv shell
$ python fedsfm_data/run.py
```

You will get a list with entries like this:

```json
{
    "number": 5244,
    "fullname": "МУДАТОВ ШАМХАЛ ДЖАЛУЕВИЧ",
    "old_fullname": "(МУДАТОВ ШАМХАН ДЖАЛУЕВИЧ)",
    "is_terrorist": true,
    "birthday": "24.05.1972",
    "age": 46,
    "gender": null,
    "place": "С. КАДИ-ЮРТ ГУДЕРМЕССКОГО РАЙОНА ЧЕЧЕНСКОЙ РЕСПУБЛИКИ;",
    "region": "Чечня"
}
```

## the idea

mad props to [lilislilit](https://github.com/lilislilit).