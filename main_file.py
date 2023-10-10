from agent import CDCDataAgent 

def main():
    # Initialize the CDCDataAgent with the data file path
    data_path = 'https://data.cdc.gov/api/views/qz99-wyhv/rows.json?accessType=DOWNLOAD'
    cdc_agent = CDCDataAgent(data_path)
    # Data validation and transformation
    cdc_agent.data_validation_and_transformation()
    # Analyze behavioral trends among unvaccinated people
    cdc_agent.analyze_behavioral_trends()
    # Offer vaccination guidance based on historical data (national scope)
    cdc_agent.offer_vaccination_guidance()
    # Offer vaccination guidance based on historical data (jurisdictional scope)
    cdc_agent.offer_vaccination_guidance()
    # Visualize data trends
    cdc_agent.visualize_data()
    # Save processed data to a file
    cdc_agent.save_data('processed_cdc_data.csv')
    # Load data from a file
    cdc_agent.load_data('processed_cdc_data.csv')
    # Remember conversations for historical context
    cdc_agent.remember_conversations("User: What are the trends in my region?")

if __name__ == "__main__":
    main()