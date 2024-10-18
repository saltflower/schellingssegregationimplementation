import pytest
from segregation_simulation import SegregationSimulation  # Adjust the import as necessary

@pytest.fixture
def setup_simulation():
    """Fixture to set up a basic simulation for testing."""
    sim = SegregationSimulation(similar=0.7, ratio=0.3, empty=0.4, size=5, delay=0.1)
    return sim

def test_grid_creation(setup_simulation):
    """Test if the grid is created correctly with the right proportions."""
    sim = setup_simulation
    grid = sim.grid
    red_count = sum(row.count('r') for row in grid)
    blue_count = sum(row.count('b') for row in grid)
    empty_count = sum(row.count('e') for row in grid)
    
    total_agents = sim.size * sim.size - empty_count
    expected_red_count = int(total_agents * sim.ratio)
    expected_blue_count = total_agents - expected_red_count
    
    assert red_count == expected_red_count, "Red agent count does not match expected."
    assert blue_count == expected_blue_count, "Blue agent count does not match expected."
    assert empty_count == int(sim.size * sim.size * sim.empty), "Empty count does not match expected."

def test_is_satisfied(setup_simulation):
    """Test the satisfaction of agents."""
    sim = setup_simulation
    # Manually create a simple grid
    sim.grid = [
        ['r', 'r', 'e', 'b', 'b'],
        ['e', 'r', 'e', 'b', 'e'],
        ['r', 'e', 'e', 'e', 'b'],
        ['e', 'e', 'e', 'r', 'r'],
        ['b', 'b', 'e', 'r', 'e']
    ]
    
    assert sim.is_satisfied(0, 0) is True, "Agent (0,0) should be satisfied."
    assert sim.is_satisfied(0, 3) is False, "Agent (0,3) should not be satisfied."

def test_update_grid(setup_simulation):
    """Test if the update_grid method works correctly."""
    sim = setup_simulation
    sim.grid = [
        ['r', 'r', 'e', 'e', 'e'],
        ['e', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'r', 'e', 'e'],
        ['b', 'e', 'e', 'e', 'e']
    ]
    
    initial_grid = [row.copy() for row in sim.grid]
    sim.update_grid()
    
    # Check that the grid has changed (at least one move should occur)
    assert sim.grid != initial_grid, "Grid should have changed after update."

def test_get_per_satisfied(setup_simulation):
    """Test the satisfaction percentage calculation."""
    sim = setup_simulation
    sim.grid = [
        ['r', 'r', 'e', 'e', 'e'],
        ['e', 'b', 'b', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'r', 'e', 'e'],
        ['b', 'e', 'e', 'e', 'e']
    ]
    
    percentage = sim.get_per_satisfied()
    assert 0 <= percentage <= 1, "Percentage of satisfied agents should be between 0 and 1."

if __name__ == "__main__":
    pytest.main()