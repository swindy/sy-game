#coding=utf-8
__author__ = 'icestar'

import os

from PyQt4.QtGui import QPixmap, QIcon, QPainter


class PixmapCache(object):
    """
    Class implementing a pixmap cache for icons.
    """
    def __init__(self):
        """
        Constructor
        """
        self.pixmapCache = {}
        self.searchPath = []

    def getPixmap(self, key):
        """
        Public method to retrieve a pixmap.

        @param key name of the wanted pixmap (string)
        @return the requested pixmap (QPixmap)
        """
        print(key)
        if key:
            try:
                return self.pixmapCache[key]
            except KeyError:

                if not os.path.isabs(key):
                    print(self.searchPath)
                    for path in self.searchPath:
                        fileName = path + "/" + key
                        print("%s, %s",path, fileName)
                        pm = QPixmap(fileName)
                        if not pm.isNull():
                            break
                    else:
                        pm = QPixmap()
                else:
                    pm = QPixmap(key)
                self.pixmapCache[key] = pm
                return self.pixmapCache[key]
        return QPixmap()

    def addSearchPath(self, path):
        """
        Public method to add a path to the search path.

        @param path path to add (string)
        """
        if not path in self.searchPath:
            self.searchPath.append(path)

pixCache = PixmapCache()


def getPixmap(key, cache=pixCache):
    """
    Module function to retrieve a pixmap.

    @param key name of the wanted pixmap (string)
    @return the requested pixmap (QPixmap)
    """
    return cache.getPixmap(key)


def getIcon(key, cache=pixCache):
    """
    Module function to retrieve an icon.

    @param key name of the wanted icon (string)
    @return the requested icon (QIcon)
    """
    return QIcon(cache.getPixmap(key))


def getSymlinkIcon(key, cache=pixCache):
    """
    Module function to retrieve a symbolic link icon.

    @param key name of the wanted icon (string)
    @return the requested icon (QIcon)
    """
    pix1 = QPixmap(cache.getPixmap(key))
    pix2 = cache.getPixmap("symlink.png")
    painter = QPainter(pix1)
    painter.drawPixmap(0, 10, pix2)
    painter.end()
    return QIcon(pix1)


def addSearchPath(path, cache=pixCache):
    """
    Module function to add a path to the search path.

    @param path path to add (string)
    """
    cache.addSearchPath(path)

