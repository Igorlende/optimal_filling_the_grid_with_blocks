from Block import Block


def algorithm(list_blocks):

    if list_blocks == False:
        return False
    if len(list_blocks) == 0:
        return False

    def first_method(list_blocks):

        #print("Блоки")
        #for block in list_blocks:
        #    print(block)

        #############################
        list_blocks.sort()

        #print("Сортовані")
        #for block in list_blocks:
        #    print(block)

        ##########################
        one_grid = [None, None, None, None]
        merriment = []

        max_height = 0
        for block in list_blocks:
            max_height = max_height + block.get_height()

        for row in range(max_height):
            merriment.append([None, None, None, None])

        max_width_grid = 4

        i = 0
        j = 0

        # цикл по блоках в списку
        for block in list_blocks:
            # чи блок записаний
            the_block_is_recorded = False
            # цикл по рядках
            for i in range(len(merriment)):
                # цикл по стовпцях
                for j in range(max_width_grid):
                    # якщо елемент порожній
                    if type(merriment[i][j]) != type(Block):
                        # вільне місце
                        free_space = False
                        i2 = i
                        j2 = j
                        try:
                            count = 0
                            for h in range(block.get_height()):
                                for w in range(block.get_width()):
                                    if merriment[i2+h][j2+w] is not None :
                                        count = count + 1
                            if count == 0:
                                free_space = True
                        except Exception:
                            continue

                        if free_space is True:
                            for h in range(block.get_height()):
                                for w in range(block.get_width()):
                                    merriment[i2 + h][j2 + w] = block
                            the_block_is_recorded = True

                    if the_block_is_recorded==True:
                        break
                if the_block_is_recorded == True:
                    break
            if the_block_is_recorded == True:
                continue

        for index in range(len(merriment)-1, 0, -1):
            count_none = 0
            for el in merriment[index]:
                if el is None:
                    count_none = count_none + 1
            if count_none == len(merriment[index]):
                merriment.pop()
            else:
                break

        return merriment

    res = first_method(list_blocks)
    return res