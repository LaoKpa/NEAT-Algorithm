class Config:
    """
    Population
    """

    population_size = 150

    # TODO: Ensure each of these are used somewhere in the code
    """
    Compatibility distance
    """
    # The coefficients used for calculating the compatibility distance between two genomes
    excess_coefficient = 1
    disjoint_coefficient = 1
    # This is for when the genes are the same so they check the similarity of the weights
    matching_genes_coefficient = 0.4

    # How close they have to be to be considered in the same species
    compatibility_threshold = 3

    """
    Mutation
    """

    # Weight changes
    weight_mutation_chance = 0.8
    weight_uniform_mutation_chance = 0.9
    weight_random_mutation_chance = 0.1
    # A range to choose from for the weight pertubation amount
    weight_range_low = -1.0
    weight_range_high = 1.0

    # This is the chance a gene is disabled if it was disabled in either parent
    change_to_disable_gene_if_either_parent_disabled = 0.75

    chance_for_mutation_without_crossover = 0.25

    inter_species_mating_rate = 0.001

    add_node_mutation_chance = 0.03
    add_connection_mutation_chance = 0.05
    # TODO: Find correct chance for these values
    remove_node_mutation_chance = 0.01
    remove_connection_mutation_chance = 0.01

    """
    Speciation
    """
    # Parameters used when check stagnation
    # Allowable number of generations before considered stagnant
    max_stagnation_generations = 15
    # Min number of species required before throwing out due to stagnation
    num_species_min = 2

    """
    Reproduction
    """
    # Minimum species size
    min_species_size = 2

    """
    Survival
    """
    # Percentage of the population which carries on un-changed(?)
    survival_threshold = 0.2
    # This means that a certain percentage of the top elite genomes will carry over to the next population un changed
    keep_unmutated_top_percentage = True # (Default should be False)