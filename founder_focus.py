
import csv

class FounderFocus:
    def __init__(self, name, sector, funding):
        self.name = name
        self.sector = sector
        self.funding = funding
    
    def is_acquisition_ready(self, buzzword_score):
        if self.funding >= 5000000 and buzzword_score >= 2:
            return True
        return False
    
    def summary(self, buzzword_score):
        acquisition_status = self.is_acquisition_ready(buzzword_score)
        return f"Startup: {self.name}\nSector: {self.sector}\nFunding: {self.funding}\nAcquisition Ready: {acquisition_status}"

def export_summary_to_txt(startup, buzzword_score, filename="founder_summary.txt"):
    summary = startup.summary(buzzword_score)
    with open(filename, "w") as file:
        file.write(summary)
    print(f"Summary exported to {filename}")

def export_to_csv(startup, filename="founder_data.csv"):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Startup Name", "Sector", "Funding", "Acquisition Ready"])
        writer.writerow([startup.name, startup.sector, startup.funding, startup.is_acquisition_ready(2)])
    print(f"Data exported to {filename}")
