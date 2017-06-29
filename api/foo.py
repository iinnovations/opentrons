from opentrons import containers, instruments, robot

p300_tips = containers.load('tiprack-200ul','E3','p10tiprack')
pcr_plate = containers.load('96-PCR-tall','C3','pcr')
template_plate = containers.load('96-PCR-flat','D3','template')

p300multi = instruments.Pipette(name="p300-multi",axis="a",max_volume=300,channels=8,tip_racks=[p300_tips])

# add 5 uL template to PCR plate 30 times.

for x in range(30):
    for i in range(12):
        p300multi.pick_up_tip(p300_tips.rows[i][0])
        p300multi.aspirate(5,template_plate.rows[i][0])
        p300multi.dispense(pcr_plate.rows[i][0]).touch_tip()
        p300multi.drop_tip(p300_tips.rows[i][0])

    robot.home(enqueue=True)
