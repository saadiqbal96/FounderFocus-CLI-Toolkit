
class FounderFocus:
    def __init__(self, name):
        self.name = name
        self.sector = None
        self.funding = 0

    def set_sector(self, sector):
        self.sector = sector

    def set_funding(self, amount):
        self.funding = amount

    def is_acquisition_ready(self):
        return self.funding >= 500_000 and self.sector in ["AI", "Fintech", "SaaS"]

    def summary(self):
        return (
            f"📊 {self.name} CLI Summary:\n"
            f"- Sector: {self.sector}\n"
            f"- Funding: ${self.funding}\n"
            f"- Acquisition-Ready: {self.is_acquisition_ready()}\n"
        )

    def export_summary_to_txt(self, filename):
        with open(filename, "w") as file:
            file.write(self.summary())
        print(f"📁 Exported summary to {filename}")

    def export_to_csv(self, filename):
        import csv
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Sector", "Funding", "AcquisitionReady"])
            writer.writerow([
                self.name,
                self.sector,
                self.funding,
                self.is_acquisition_ready(),
            ])
        print(f"📊 Exported data to {filename}")
