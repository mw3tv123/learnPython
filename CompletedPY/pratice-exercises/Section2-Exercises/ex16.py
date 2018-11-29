"""
Write a program that visualize the steps to solve Tower of Hanoi problem.

NOTE: The number of disks is provided by user.

Example:

   1       2       3
   |       |       |
  #|#      |       |
 ##|##     |       |
###|###    |       |
---+--- ---+--- ---+---

   .---------------.
                   V
   1       2       3
   |       |       |
   |       |       |
 ##|##     |       |
###|###    |      #|#
---+--- ---+--- ---+---

   .-------.
           V
   1       2       3
   |       |       |
   |       |       |
   |       |       |
###|###  ##|##    #|#
---+--- ---+--- ---+---

           .-------.
           V
   1       2       3
   |       |       |
   |       |       |
   |      #|#      |
###|###  ##|##     |
---+--- ---+--- ---+---

   .---------------.
                   V
   1       2       3
   |       |       |
   |       |       |
   |      #|#      |
   |     ##|##  ###|###
---+--- ---+--- ---+---

   .-------.
   V
   1       2       3
   |       |       |
   |       |       |
   |       |       |
  #|#    ##|##  ###|###
---+--- ---+--- ---+---

           .-------.
                   V
   1       2       3
   |       |       |
   |       |       |
   |       |     ##|##
  #|#      |    ###|###
---+--- ---+--- ---+---

   .---------------.
                   V
   1       2       3
   |       |       |
   |       |      #|#
   |       |     ##|##
   |       |    ###|###
---+--- ---+--- ---+---

ET: 8 hours
"""


def tower_of_Hanoi(disk, head=[], mid=[], end=[]):
    if disk == 1:
        head.remove(disk)
        end.append(disk)
        print(head, mid, end)
    else:
        tower_of_Hanoi(disk - 1, head, mid, end)
        if mid[0] < disk:
            head.remove(disk)
            mid.append(disk)
        elif end[0] < disk:
            # TODOs code
            pass
    return head, mid, end


def main():
    head = [1, 2, 3]
    mid = []
    end = []
    disk = int(input(">>> Enter number of disk: "))
    print(tower_of_Hanoi(disk, head, mid, end))


if __name__ == "__main__":
    main()