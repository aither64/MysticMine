
import os

from monorail.koon.res import resman

from monorail.pickups import *
from monorail.player import *
from monorail.tiles import *

class TestFlag:

    def test_dirs( self ):
        # Given
        tile = Tile( Vec3D(), Tile.Type.FLAT )
        goldcar = GoldCar( TrailPosition( tile, 0 ), 0 )
        flag = Flag(goldcar)

        # When


        # Then

class TestDynamite:

    def test_is_good( self ):
        dynamite = Dynamite()

        assert not dynamite.is_good()
        assert dynamite.is_bad()

class TestLamp:

    def test_is_good( self ):
        lamp = Lamp()

        assert lamp.is_good()
        assert not lamp.is_bad()

