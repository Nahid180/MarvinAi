import main
import dataset_creator.create as create

print("Restore started.....")

create.db.drop_all()
create.db.create_all()

for i in main.Marvin.query.all():
    create.db.session.add(create.Marvin(speaker=i.speaker,reply=i.reply,tag=i.tag))
    create.db.session.commit()

print("Done restoring.....")
