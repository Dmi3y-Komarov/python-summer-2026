from player import Player
from game import Game

def main():

    game = Game()

    game.choose_character()

    playing = True
    while playing:
        if not game.player.is_alive():
            if not game.game_over():
                playing = False
                break
            else:
                continue

        game.player.show_stats()
        game.show_location()
        
        choice = input("\nТвой выбор: ").strip()

        try:
            loc = game.get_current_location()
            action = loc["actions"][int(choice)-1]
            game.handle_action(action)
        except ValueError:
            print("Ошибка: неверный ввод!")

    print("\nИгра окончена. До скорых волнующиз встреч!")

if __name__ == "__main__":
    main()

