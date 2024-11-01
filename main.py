class Musician:
    def __init__(self, id, last_name, experience, orchestra_id):
        self.id = id 
        self.last_name = last_name  
        self.experience = experience  
        self.orchestra_id = orchestra_id  

    def __repr__(self):
        return f"Музыкант(id={self.id}, фамилия='{self.last_name}', опыт={self.experience}, orchestra_id={self.orchestra_id})"

class Orchestra:
    def __init__(self, id, name):
        self.id = id  
        self.name = name 
    def __repr__(self):
        return f"Оркестр(id={self.id}, название='{self.name}')"

class MusicianOrchestra:
    def __init__(self, musician_id, orchestra_id):
        self.musician_id = musician_id  
        self.orchestra_id = orchestra_id  

    def __repr__(self):
        return f"Связь(музыкант_id={self.musician_id}, оркестр_id={self.orchestra_id})"

orchestras = [
    Orchestra(1, 'Симфонический Оркестр'),
    Orchestra(2, 'Камерный Оркестр'),
    Orchestra(3, 'Джазовый Оркестр')
]

musicians = [
    Musician(1, 'Александров', 5, 1),
    Musician(2, 'Иванов', 3, 2),
    Musician(3, 'Антонов', 7, 1),
    Musician(4, 'Борисов', 2, 3),
    Musician(5, 'Андреев', 4, 3)
]

musician_orchestra_links = [
    MusicianOrchestra(1, 1),
    MusicianOrchestra(2, 2),
    MusicianOrchestra(3, 1),
    MusicianOrchestra(3, 2),
    MusicianOrchestra(4, 3),
    MusicianOrchestra(5, 3),
    MusicianOrchestra(5, 1)
]


print("Запрос 1: Музыканты, у которых фамилия начинается с 'А', и их оркестры:\n")

filtered_musicians = [m for m in musicians if m.last_name.startswith('А')]

for musician in filtered_musicians:
    orchestra = next((o for o in orchestras if o.id == musician.orchestra_id), None)
    if orchestra:
        print(f"Музыкант: {musician.last_name}, Оркестр: {orchestra.name}")


print("\nЗапрос 2: Оркестры с минимальным опытом музыкантов, отсортированные по минимальному опыту:\n")

orchestra_experience = {}
for musician in musicians:
    orchestra_id = musician.orchestra_id
    orchestra_experience.setdefault(orchestra_id, []).append(musician.experience)

orchestra_min_exp = [
    (next(o.name for o in orchestras if o.id == orchestra_id), min(experiences))
    for orchestra_id, experiences in orchestra_experience.items()
]

orchestra_min_exp_sorted = sorted(orchestra_min_exp, key=lambda x: x[1])

for name, min_exp in orchestra_min_exp_sorted:
    print(f"Оркестр: {name}, Минимальный опыт музыкантов: {min_exp} лет")

print("\nЗапрос 3: Все связанные музыканты и оркестры, отсортированные по фамилии музыкантов:\n")

musician_orchestra_list = [
    (next(m.last_name for m in musicians if m.id == link.musician_id),
     next(o.name for o in orchestras if o.id == link.orchestra_id))
    for link in musician_orchestra_links
]

musician_orchestra_list_sorted = sorted(musician_orchestra_list, key=lambda x: x[0])

for last_name, orchestra_name in musician_orchestra_list_sorted:
    print(f"Музыкант: {last_name}, Оркестр: {orchestra_name}")
