def manapotion(caster, target):
    totalMana = caster.getManaTotal() + 1
    caster.setManaTotal(totalMana)


def fireball(caster, target):
    totalMana = caster.getManaTotal() - 4
    caster.setManaTotal(totalMana)
    lifeTotal = target.getLifeTotal() - 6
    target.setLifeTotal(lifeTotal)


def spring(caster, target):
    totalMana = caster.getManaTotal() - 4
    caster.setManaTotal(totalMana)
    lifeTotal = caster.getLifeTotal() + 6
    caster.setLifeTotal(lifeTotal)


def sprint(caster, target):
    totalMana = caster.getManaTotal() - 2
    caster.setManaTotal(totalMana)
    manaTotal = caster.getManaTotal() + 4
    caster.setManaTotal(manaTotal)


def immobilize(caster, target):
    totalMana = caster.getManaTotal() - 2
    caster.setManaTotal(totalMana)
    manaTotal = target.getManaTotal() - 4
    target.setManaTotal(manaTotal)
    if target.getManaTotal() < 0:
        target.setManaTotal(0)
