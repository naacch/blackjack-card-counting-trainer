from logic.card import CardName


HI_LO: dict[CardName: int] = {
    CardName.TWO: 1,
    CardName.THREE: 1,
    CardName.FOUR: 1,
    CardName.FIVE: 1,
    CardName.SIX: 0,
    CardName.SEVEN: 0,
    CardName.EIGHT: 0,
    CardName.NINE: 0,
    CardName.TEN: -1,
    CardName.JACK: -1, 
    CardName.QUEEN: -1,
    CardName.KING: -1,
    CardName.ACE: -1
}