#include <iostream>
#include <boost/random.hpp>
#include <boost/chrono.hpp>
#include <math.h>

double GenerateRandomNumber(double start, double end)
{
	boost::chrono::system_clock::time_point now = boost::chrono::system_clock::now();
	std::string count = std::to_string(now.time_since_epoch().count());
	int system_time = std::stoi(count.substr(count.size()-7,7));
	boost::random::mt19937 gen{static_cast<std::uint32_t>(system_time)}; 
	boost::random::uniform_real_distribution<> dist{start,end};
	return dist(gen);
}

int SelectionWithProbability(std::vector<double>& vec)
{
	double sum = 0;
	for(int i=0; i<vec.size(); i++) { sum = sum + vec[i]; }
	double random_number = GenerateRandomNumber(0, sum);

	int pos = -1;
	double sum_ = 0;
	for(int i=0; i<vec.size(); i++)
	{
		sum_ = sum_ + vec[i];
		if(random_number < sum_) { pos = i; break; }
	}
	return pos;
}

std::vector<int> SelectionWithProbability(std::vector<double>& vec, int number)
{
	std::vector<int> result;
	for(int i=0;i<vec.size();i++){result.push_back(0);}
	for(int i=0;i<number; i++)
	{
		int pos = SelectionWithProbability(vec);
		result[pos] = result[pos] + 1;
	}
	return result;
}

namespace problem
{
	namespace SCH 
	{
		double TargetFunction1(double x)
		{
			return x * x;
		}
		double TargetFunction2(double x)
		{
			return (x - 2) * (x - 2);
		}
	}
	namespace POL
	{
		double TargetFunction1(double x1, double x2)
		{
			double a1 = 0.5 * std::sin(1) - 2 * std::cos(1) 
						+ std::sin(2) - 1.5 * std::cos(2);
			double a2 = 1.5 * std::sin(1) - std::cos(1) 
						+ 2 * std::sin(2) - 0.5 * std::cos(2);
			double b1 = 0.5 * std::sin(x1) - 2 * std::cos(x1) 
						+ std::sin(x2) - 1.5 * std::cos(x2);
			double b2 = 1.5 * std::sin(x1) - std::cos(x1) 
						+ 2 * std::sin(x2) - 0.5 * std::cos(x2);
			return 1 + (a1 - b1) * (a1 - b1) + (a2 - b2) * (a2 - b2);
		}

		double TargetFunction2(double x1, double x2)
		{
			return (x1 + 3) * (x1 + 3) + (x2 + 1) * (x2 + 1);
		}
	}
}

class Chromosome 
{
	public:
		Chromosome()
		{
			double ele0 = GenerateRandomNumber(-3,3);
			double ele1 = GenerateRandomNumber(-3,3);
			this->m_chromosome = std::make_tuple(ele0, ele1);
			UpdateFitness();
		}
		Chromosome(std::tuple<double, double> chromosome)
		{
			this->m_chromosome = chromosome;
			UpdateFitness();
		}
		std::tuple<double, double> GetChromosome()
		{
			return m_chromosome;
		}
		std::tuple<double, double> GetFitness()
		{
			return m_fitness;
		}
		Chromosome CrossoverOpeartor(Chromosome& another) 
		{
			std::tuple<double, double> chromosome = another.GetChromosome();
			double ele1 = std::get<0>(chromosome) + std::get<0>(m_chromosome);
			double ele2 = std::get<1>(chromosome) + std::get<1>(m_chromosome);
			return Chromosome(std::make_tuple(ele1, ele2));
		}
		void MutationOperator()
		{
			double ele1 = std::get<0>(m_chromosome) + GenerateRandomNumber(-2,2);
			double ele2 = std::get<1>(m_chromosome) + GenerateRandomNumber(-2,2);
			m_chromosome = std::make_tuple(ele1, ele2);
			UpdateFitness();
		}
	private:
		void UpdateFitness()
		{
			double ele0 =problem::POL::TargetFunction1(std::get<0>(m_chromosome)
										  ,std::get<1>(m_chromosome));
			double ele1 =problem::POL::TargetFunction2(std::get<0>(m_chromosome)
										  ,std::get<1>(m_chromosome));
			m_fitness = std::make_tuple(ele0, ele1);
		}

	private:
		std::tuple<double, double> m_chromosome;
		std::tuple<double, double> m_fitness;
};


class GeneticAlgorithm {
	public:
		void initial(int poplulation)
		{
			for(int i = 0;i < poplulation; i++)
			{
				Chromosome temp;
				m_population.push_back(temp);
			}
		}
		void Selection()
		{
			std::vector<double> fitness_vec;
			for(int i=0; i<m_population.size(); i++)
			{
				double weight0 = GenerateRandomNumber(0,1);
				double weight1 = 1 -weight0;
				std::tuple<double, double> fitness = m_population[i].GetFitness();
				double weighted_fitness = std::get<0>(fitness) * weight0
										+ std::get<1>(fitness) * weight1;
				fitness_vec.push_back(weighted_fitness);
			}
			std::vector<int> selection_index = SelectionWithProbability(fitness_vec, 5);
			std::vector<Chromosome> new_population;
			for(int i=0; i< selection_index.size(); i++)
			{
				for(int m=0; m<selection_index[i]; m++)
				{
					new_population.push_back(m_population[i]);
				}
			}
			m_population = new_population;
		}


		void DisplayPopulation()
		{
			for(int i = 0; i < m_population.size(); i++)
			{
				std::cout<<"chromosome: "<<std::get<0>(m_population[i].GetChromosome())
				         <<" "<<std::get<1>(m_population[i].GetChromosome())
						 <<" fitness: "<<std::get<0>(m_population[i].GetFitness())
						 <<" "<<std::get<1>(m_population[i].GetFitness())
						 <<std::endl;
			}
		}
	private:
		std::vector<Chromosome> m_population;
};




int main()
{
	GeneticAlgorithm ga;
	ga.initial(10);
	ga.DisplayPopulation();
	std::cout<<"***************************"<<std::endl;
	ga.Selection();
	ga.DisplayPopulation();
}

