import create
import main

main.db.create_all()

for i in create.Marvin.query.all():
    main.db.session.add(main.Marvin(speaker=i.speaker,reply=i.reply,tag=i.tag))
    main.db.session.commit()

print(main.Marvin.query.all())

