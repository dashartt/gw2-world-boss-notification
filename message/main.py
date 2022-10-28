def message_world_boss_alert(avaliable_world_boss):
    informations = list()

    informations.append("""
# Avaliables:

    """)

    for world_boss in avaliable_world_boss:
        informations.append(
            f"""
name: {world_boss['name']}
starts at: {world_boss['start_time']}
zone: {world_boss['zone']}
area: {world_boss['area']}
___________________________
            """
        )
    
    return "".join(informations)