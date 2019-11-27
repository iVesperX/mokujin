import discord


def move_embed(character, move):
    """Returns the embed message for character and move"""
    embed = discord.Embed(title=character['proper_name'],
                          colour=0x00EAFF,
                          url=character['online_webpage'],
                          description='**Move: ' + move['Command'] + '**')

    embed.set_thumbnail(url=character['portrait'])
    embed.add_field(name='Property', value=move['Hit level'])
    embed.add_field(name='Damage', value=move['Damage'])
    embed.add_field(name='Startup', value='i' + move['Start up frame'])

    if 'Throw' in move['Notes']:
        # throw
        embed.add_field(name='Result Position', value=move['Success frame'])
        embed.add_field(name='Break Type', value=move['Break input'])
        embed.add_field(name='Break Window', value=move['Break frame'])
    else:
        # attack
        embed.add_field(name='Block', value=move['Block frame'])
        embed.add_field(name='Hit', value=move['Hit frame'])
        embed.add_field(name='Counter Hit', value=move['Counter hit frame'])

    embed.add_field(name='Notes', value=(move['Notes'] if move['Notes'] else "-"))
    if move['Gif']:
        embed.add_field(name='Gif', value=move['Gif'], inline=False)

    return embed


def move_list_embed(character, move_list, move_type):
    """Returns the embed message for a list of moves matching to a special move type"""
    desc_string = ''
    for move in move_list:
        desc_string += move + '\n'

    embed = discord.Embed(title=character['proper_name'] + ' ' + move_type.lower() + ':',
                          colour=0x00EAFF,
                          description=desc_string)
    return embed


def error_embed(err):
    embed = discord.Embed(title='Error',
                          colour=0xFF4500,
                          description=err)
    return embed


def success_embed(message):
    embed = discord.Embed(title='Success',
                          colour=0x3ddb2c,
                          description=message)
    return embed


def similar_moves_embed(similar_moves):
    embed = discord.Embed(title='Move not found', colour=0xfcba03,
                          description='Similar moves:\n**{}**'
                          .format('** **\n'.join(similar_moves)))
    return embed


def help_embed():
    text = "" \
           "!character move     - get frame data of a move from a character \n" \
           "!clear-messages        - deletes bot's last own messages\n" \
           "?feedback message   - send message including sender name to the devs  \n\n " \
            "The bot automatically deletes it's own messages after 20 seconds except in channel with the 'tekken' or 'frame' in it"
    embed = discord.Embed(title='Commands', description=text, colour=0x37ba25)
    embed.set_author(name='Author: Tib')

    return embed


def thank_embed():
    text = "\n\n" \
           "Much thanks and love to T7Chicken Team, Ruxx, BKNR, Vesper, Maxwell, Dramen, Dreamotion, Jacket and Cangu. \n\n" \
           "This project won't be possible without you guys <3"
    embed = discord.Embed(title='Commands', description=text, colour=0x37ba25)
    embed.set_author(name='Author: Tib')
    return embed
