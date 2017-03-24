import pytest
import mock
from mesh3d.shapes.mesh import Mesh
from mesh3d.shapes.vertex import Vertex
from mesh3d.shapes.face import Face


class TestMesh:

    def test_mesh_contructor(self):
        """Constructor test."""
        vertices_stub = mocker.stub("vertices_stub")
        faces_stub = mocker.stub("faces_stub")
        mesh = Mesh(vertices_stub, faces_stub)
        assert mesh is not None
