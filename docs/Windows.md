# How to compile shit with chowdren speedun edition // will polish these later

1. Install/extract the following

[Clickteam 2.5](https://store.steampowered.com/app/248170/Clickteam_Fusion_25/)

[VCForPython27.msi](/Files/VCForPython27.msi)

[cmake-3.29.0-rc2-windows-x86_64.zip](/Files/cmake-3.29.0-rc2-windows-x86_64.zip)

[python-2.7.18.amd64.msi](/Files/python-2.7.18.amd64.msi)

[Mingw]()

[Visual studio 2015](https://archive.org/details/MS_VisualStudioCommunity-2015) ???

[Anaconda](https://github.com/fnmwolf/Anaconda)

# WARNING ❗

Converting the executable to chowdren's format

```sh
cd Chowdren
python -m chowdren.run <exename> <outdir>
```

It should convert the game's assets to `Assets.dat` format and generate bunch of .cpp files

Open Cmake GUI and set the folder with `Assets.dat` as the `Build` folder. Set the `Build` folder inside that folder named `build`

```sh
```
