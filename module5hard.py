class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __repr__(self):
        mins = f'{self.duration // 60}'
        secs = f'{self.duration % 60}' #  Или: f'{self.duration % 60 if self.duration % 60 > 10 else "0" + str(self.duration % 60)}'
        if self.duration % 60 < 10:
            secs = '0' + secs
        return self.title + f' ({mins}:{secs})'


class User:
    def __init__(self, nn: str, ps: int, age: int):
        self.nickname = nn
        self.password = ps
        self.age = age

    def __repr__(self):
        return self.nickname


class UrTube:
    def __init__(self, users: list[User] = None, videos: list[Video] = None):
        self.users = users
        self.videos = videos
        self.current_user = None
        if self.users is None:
            self.users = []
        if self.videos is None:
            self.videos = []

    def register(self, nn: str, ps: str, age: int):
        for u in self.users:
            if u.nickname == nn:
                print(f'Пользователь {nn} уже существует')
                return
        self.users.append(User(nn, hash(ps), age))
        self.log_in(nn, ps)


    def log_in(self, nickname: str, password: str):
        found = False
        for u in self.users:
            if u.nickname == nickname:
                if u.password == hash(password):
                    self.current_user = u
                    found = True
                else:
                    print('Wrong password.')
        if not found:
            print('Nonexistent user.')

    def log_out(self):
        self.current_user = None

    def add_videos(self, *new_videos: Video):
        for nv in new_videos:
            found_same = False
            for v in self.videos:
                if v.title == nv.title:
                    found_same = True
                    break
            if not found_same:
                self.videos.append(nv)

    def get_videos(self, search: str) -> list[Video]:
        match = search.lower()
        out = []
        for f in self.videos:
            if match in f.title.lower():
                out.append(f)
        return out

    def watch_video(self, title: str):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return
        from time import sleep
        watch = None
        for w in self.videos:
            if w.title == title:
                watch = w
                break

        if watch is not None:
            if watch.adult_mode:
                if self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу.')
                    return
            while watch.time_now <= watch.duration:
                print(watch.time_now, end= ' ')
                sleep(1)
                watch.time_now += 1
            watch.time_now = 0
            print('Конец видео.')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('WikiLeaks: Charlie Caplain body whereabouts 2024', 2, adult_mode=True)

# Добавление видео
ur.add_videos(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('2024'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('WikiLeaks: Charlie Caplain body whereabouts 2024')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('WikiLeaks: Charlie Caplain body whereabouts 2024')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('WikiLeaks: Charlie Caplain body whereabouts 2024')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
