#!/opt/pwn.college/python

def print_instructions():
    print("""
    Another day, another email! Good 'ol William Kiffin
    has emailed you again asking you to add his user account to a new group.

        Dear beloved System Administrator,

        I am trying to use the "docker" command on my computer, but it's not
        working unless I run it as administrator! Could you add my user to the "docker"
        group please?

        Sincerely,
        William Kiffin

        P.S. My account name is 'wkiffin'.

    Use the 'usermod' command to add the 'wkiffin' user to the 'docker' group!

          'usermod -aG docker wkiffin'
    """)

def main():
    print("WIP")

if __name__ == "__main__":
    main()
