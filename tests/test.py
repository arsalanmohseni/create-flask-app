from rich.prompt import Confirm

is_rich_great = Confirm.ask("Do you like rich?")
print(is_rich_great)
