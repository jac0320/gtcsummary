# Exploring Factory-Scale Digital Twin Simulation

**Speakers**  
- **John Pritchard** (Business Manager, Emulate3D) – Responsible for integration and business operations of Emulate3D within Rockwell Automation.  
- **Roger Kassouf** (Applications Consultant Manager, Emulate3D) – Leads the Applications Consultancy team, focusing on complex system builds, virtualization, and motion control.

---

## Overview

Rockwell Automation’s **Emulate3D** platform enables **digital twins** of manufacturing equipment and entire **factory environments**. The solution integrates with **NVIDIA Omniverse** to handle **large-scale** models, enabling **modular** and **collaborative** simulations for engineering teams. This approach streamlines:

- **Demonstration** (visualizing system models in VR or video)  
- **Simulation** (analyzing throughput, identifying bottlenecks)  
- **Virtual Commissioning** (connecting real PLC or robot controllers to the simulated environment)

---

## Key Points

### 1. Need for Scalable Digital Twins
- **Factories are complex**: Thousands of moving parts, high-speed machinery, multiple domains.  
- **Collaboration** is essential: Mechanical, electrical, controls, robotics, and process experts must combine inputs.  
- **Modular modeling**: Domain experts build sub-models; these are aggregated for a factory-scale view.

### 2. Emulate3D and Omniverse Integration
- **USD Data Exchange**: Allows rapid conversion of Emulate3D models into **Universal Scene Description (USD)** format.  
- **NVIDIA Omniverse**: Aggregates Emulate3D models with building/facility data for **photorealistic** and **collaborative** simulation.  
- **Multi-model approach**: Large or dynamic sections can be split across different virtual machines, then merged for a unified view.

### 3. Emulate3D Capabilities
1. **Demonstration**  
   - Rapidly create dynamic system models with generic objects or imported CAD.  
   - Produce videos or immersive **VR** experiences.  
2. **Virtual Commissioning**  
   - Connect simulation to **real controls** (PLCs, robot controllers).  
   - Validate logic offline, reducing on-site errors.  
3. **Simulation**  
   - Test system throughput, identify bottlenecks, and optimize resource allocation.  
   - Run **what-if** scenarios to reduce investment risk.

### 4. Recent Case Studies & Examples
- **Automotive Assembly Cell**: Using Omniverse for large-scale assembly simulations.  
- **Logistics “Lights-out” Facility**: Combined Emulate3D models with building data to validate fully automated warehouse operations.  
- **Virtual Commissioning** with iTRAK configuration and O-Ring installation demos.

### 5. Factory Test & Deployment
- **Emulate3D Factory Test**:  
  - Multi-model system running on separate VMs/servers.  
  - **NVIDIA Omniverse** for centralized rendering and **photorealistic** visualization.  
- **Deployment Architecture**:  
  - Multiple Emulate3D nodes feed model data to Omniverse.  
  - Real or virtual PLCs connect to each Emulate3D instance.  

### 6. Benefits & Future Directions
- **Faster Time to Value**: Simulation + VR + virtual commissioning significantly reduces commissioning risk.  
- **Improved Collaboration**: Teams can refine mechanical, electrical, and controls aspects in a shared environment.  
- **Scalable**: Emulate3D with Omniverse handles larger, more complex manufacturing lines.  
- **Ongoing Work**: Enhancing performance, refining modular workflows, adding new features for large-scale industrial clients.

---

## Conclusion
- Emulate3D provides **physics-based digital twins** for manufacturing systems.  
- **Factory-scale** simulations are possible via modular models aggregated in **NVIDIA Omniverse**.  
- This enables **photorealistic**, **collaborative**, and **highly dynamic** digital twins for commissioning, throughput analysis, and demonstration.  
- **Visit Booth #137** at GTC for a **live demo** or learn more at [www.rockwellautomation.com](https://www.rockwellautomation.com).

