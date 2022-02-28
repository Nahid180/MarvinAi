import main
import restore

print("Restore started.....")

restore.db.drop_all()
restore.db.create_all()

for i in main.Marvin.query.all():
    restore.db.session.add(restore.Marvin(speaker=i.speaker,reply=i.reply,tag=i.tag))
    restore.db.session.commit()

print("Done restoring.....")
