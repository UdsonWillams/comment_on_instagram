import sqlite3



class AppDB:
    """Create app Database"""

    def __init__(self) -> None:
        self.database = sqlite3.connect("profile.db")
        self.cursor = self.database.cursor()             
        try:
            self.cursor.execute(
                "CREATE TABLE perfis (perfil text)"
            )
            self.database.commit()
        except sqlite3.OperationalError:
            pass

    def create_instagram_profile(self, profile: str) -> bool:
        try:
            self.cursor.execute(
                "INSERT INTO profile VALUES('"+profile+"')")
            self.database.commit()            
        except Exception:
            return False
        return True
