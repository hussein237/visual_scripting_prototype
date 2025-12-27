#!/usr/bin/env python3
import subprocess
import sys
import os
from pathlib import Path

class Builder:
    def __init__(self):
        self.platform = sys.platform
        self.compiler = "clang++"
        self.flags = [
            "-std=c++17",
            "-O2",
            "-g",
            "-Wall",
            "-Wextra"
        ]

        self.root = Path(__file__).parent
        self.src_dir = self.root / "src"
        self.build_dir = self.root / "build"
        self.imgui_dir = self.root / "thirdparty" / "imgui"

        self.output = self.build_dir / "application"

    def find_sources(self):
        """Recherche récursive de tous les fichiers .cpp"""
        return [str(p) for p in self.src_dir.rglob("*.cpp")]

    def get_includes(self):
        """Dossiers d'inclusion"""
        return [
            f"-I{self.src_dir}",
            f"-I{self.imgui_dir}",
        ]

    def get_libraries(self):
        """Librairies système"""
        libs = []

        if self.platform == "win32":
            libs.extend([
                "-lSDL3",
                "-limm32",
                "-loleaut32"
            ])
        elif self.platform == "darwin":
            libs.extend([
                "-lSDL3",
                "-framework", "Cocoa"
            ])
        else:  # Linux
            libs.extend([
                "-lSDL3",
                "-ldl",
                "-lpthread"
            ])

        return libs

    def build(self):
        print("🔧 Build en cours...")

        self.build_dir.mkdir(exist_ok=True)

        sources = self.find_sources()
        if not sources:
            print(" Aucun fichier source trouvé.")
            sys.exit(1)

        cmd = [
            self.compiler,
            *self.flags,
            *self.get_includes(),
            *sources,
            *self.get_libraries(),
            "-o",
            str(self.output)
        ]

        print(" Commande :", " ".join(cmd))
        subprocess.run(cmd, check=True)
        print(" Build terminé avec succès.")

    def run(self):
        if not self.output.exists():
            print(" Application non compilée. Lancez le build d'abord.")
            return

        print("🚀 Lancement de l'application...")
        subprocess.run([str(self.output)])

    def clean(self):
        if self.build_dir.exists():
            print("🧹 Nettoyage du build...")
            for file in self.build_dir.iterdir():
                file.unlink()
            self.build_dir.rmdir()
            print(" Build nettoyé.")

if __name__ == "__main__":
    builder = Builder()

    if len(sys.argv) == 1:
        builder.build()
    elif sys.argv[1] == "run":
        builder.run()
    elif sys.argv[1] == "clean":
        builder.clean()
    else:
        print("Usage:")
        print("  python build.py        # build")
        print("  python build.py run    # run")
        print("  python build.py clean  # clean")
