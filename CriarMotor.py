#Author - Sarah Rodi Thomaz
#Description - Desenha uma estrutura de motor-foguete para combustível sólido

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def create_nozzle(raio_interno, radius_nozzle, width_diverg, height_converg, inner_diameter, distance_first_cut, circle_diameter_mm, qty_first_cut, t_mm):
    """
    Função para desenhar o bocal de um motor de foguete no Fusion 360.
    
    Parâmetros:
    - raio_interno: raio interno do tubo do motor.
    - radius_nozzle: raio do bocal na saída.
    - width_diverg: largura da seção divergente do bocal.
    - height_converg: altura da seção convergente do bocal.
    - inner_diameter: diâmetro interno da seção de transição.
    - distance_first_cut: distância da base à fileira de furos.
    - circle_diameter_mm: diâmetro dos furos.
    - qty_first_cut: quantidade de furos.
    """
    app = adsk.core.Application.get()
    ui = app.userInterface
    design = app.activeProduct

    # Get the root component of the active design.
    root_comp = design.rootComponent

    # Create a new sketch on the XY plane.
    sketches = root_comp.sketches
    xz_plane = root_comp.xZConstructionPlane
    sketch = sketches.add(xz_plane)

    # Draw the square geometry.
    lines = sketch.sketchCurves.sketchLines
    start_point = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut-1.5*circle_diameter_mm)
    end_point1 = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut+ circle_diameter_mm)
    end_point2 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, distance_first_cut+ circle_diameter_mm)
    end_point3 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, distance_first_cut+ 2* circle_diameter_mm)
    end_point4 = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut+2* circle_diameter_mm)
    end_point5 = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut+2.5* circle_diameter_mm)
    end_point6 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, distance_first_cut+2.5* circle_diameter_mm)
    end_point7 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, distance_first_cut+3.5* circle_diameter_mm)
    end_point8 = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut+3.5* circle_diameter_mm)
    end_point9 = adsk.core.Point3D.create(raio_interno-0.05, 0, distance_first_cut+4* circle_diameter_mm)
    end_point10 = adsk.core.Point3D.create(raio_interno-0.3, 0, distance_first_cut+4* circle_diameter_mm+0.5)
    end_point11 = adsk.core.Point3D.create(raio_interno - 0.5, 0, distance_first_cut+4* circle_diameter_mm+0.5)
    end_point12 = adsk.core.Point3D.create(radius_nozzle, 0, (distance_first_cut+4* circle_diameter_mm+0.3 - height_converg) )
    end_point13 = adsk.core.Point3D.create(radius_nozzle, 0, (distance_first_cut+4* circle_diameter_mm+0.3 - height_converg - radius_nozzle))
    end_point14 = adsk.core.Point3D.create(width_diverg, 0, (distance_first_cut+4* circle_diameter_mm+0.3 - height_converg - radius_nozzle - 2*inner_diameter))
    end_point15 = adsk.core.Point3D.create(width_diverg + 0.5, 0, (distance_first_cut+4* circle_diameter_mm+0.3 - height_converg - radius_nozzle - 2*inner_diameter))
    end_point16 = adsk.core.Point3D.create(width_diverg + 0.5, 0, distance_first_cut-1.5*circle_diameter_mm)

    line1 = lines.addByTwoPoints(start_point, end_point1)
    line2 = lines.addByTwoPoints(end_point1, end_point2)
    line3 = lines.addByTwoPoints(end_point2, end_point3)
    line4 = lines.addByTwoPoints(end_point3, end_point4)
    line5 = lines.addByTwoPoints(end_point4, end_point5)
    line6 = lines.addByTwoPoints(end_point5, end_point6)
    line7 = lines.addByTwoPoints(end_point6, end_point7)
    line8 = lines.addByTwoPoints(end_point7, end_point8)
    line9 = lines.addByTwoPoints(end_point8, end_point9)
    line10 = lines.addByTwoPoints(end_point9, end_point10)
    line11 = lines.addByTwoPoints(end_point10, end_point11)
    line12 = lines.addByTwoPoints(end_point11, end_point12)
    line13 = lines.addByTwoPoints(end_point12, end_point13)
    line14 = lines.addByTwoPoints(end_point13, end_point14)
    line15 = lines.addByTwoPoints(end_point14, end_point15)
    line16 = lines.addByTwoPoints(end_point15, end_point16)
    line17 = lines.addByTwoPoints(end_point16, start_point)

     # Add a fillet at end_point3 with a radius of 5mm.
    sketch.sketchCurves.sketchArcs.addFillet(line16, end_point16, line17, end_point16, 0.5)
    sketch.sketchCurves.sketchArcs.addFillet(line11, end_point11, line12, end_point11, 0.2)
    sketch.sketchCurves.sketchArcs.addFillet(line13, end_point13, line14, end_point13, radius_nozzle)
    sketch.sketchCurves.sketchArcs.addFillet(line12, end_point12, line13, end_point12, radius_nozzle)
    sketch.sketchCurves.sketchArcs.addFillet(line14, end_point14, line15, end_point14, 0.2)
    sketch.sketchCurves.sketchArcs.addFillet(line1, end_point1, line2, end_point1, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line2, end_point2, line3, end_point2, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line3, end_point3, line4, end_point3, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line4, end_point4, line5, end_point4, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line5, end_point5, line6, end_point5, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line6, end_point6, line7, end_point6, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line7, end_point7, line8, end_point7, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line8, end_point8, line9, end_point8, circle_diameter_mm/10)
   
    # Finish the sketch.
    sketch.isComputeDeferred = False

    # Create the revolve feature.
    revolves = root_comp.features.revolveFeatures
    height_line = lines.item(2)  # Assuming the height line is the third line created.
    rev_input = revolves.createInput(sketch.profiles.item(0), root_comp.yConstructionAxis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    rev_input.setAngleExtent(True, adsk.core.ValueInput.createByReal(2 * math.pi))
    rev = revolves.add(rev_input)

    # Calculate the offset for the construction plane in mm.
    offset_value_mm = (raio_interno) * 10

    # Create a plane parallel to the YZ plane with the calculated offset.
    planes = root_comp.constructionPlanes
    yz_plane_input = planes.createInput()
    yz_plane_input.setByOffset(root_comp.yZConstructionPlane, adsk.core.ValueInput.createByString(f'{offset_value_mm} mm'))
    yz_plane = planes.add(yz_plane_input)

    # Create a circle with a diameter defined by the user on the displaced plane.
    circle_radius_mm = circle_diameter_mm / 2  # Radius is half the diameter

    # Create the first circle for the first hole.
    first_circle_center = adsk.core.Point3D.create(0, distance_first_cut, 0)  # Fixed position in X and Z axes, defined position in Y axis
    first_circle_sketch = sketches.add(yz_plane)
    first_circle = first_circle_sketch.sketchCurves.sketchCircles.addByCenterRadius(first_circle_center, circle_radius_mm)
    first_circle_profile = first_circle_sketch.profiles.item(0)
   
    # Extrude cut the first circle with a depth equal to raio_interno.
    depth_hole2 = -t_mm -10
    extrudes = root_comp.features.extrudeFeatures
    ext_input = extrudes.createInput(first_circle_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
    distance_input = adsk.core.ValueInput.createByString(f'{depth_hole2} mm')
    ext_input.setDistanceExtent(True, distance_input)
    first_cut = extrudes.add(ext_input)

    # Circular patterns
    circular_patterns = root_comp.features.circularPatternFeatures

    # Create a collection for the first cut features.
    first_cut_features_collection = adsk.core.ObjectCollection.create()
    first_cut_features_collection.add(first_cut)

    # Create the circular pattern for the cut features.
    first_pattern_input = circular_patterns.createInput(first_cut_features_collection, root_comp.yConstructionAxis)
    first_pattern_input.quantity = adsk.core.ValueInput.createByString(str(qty_first_cut))
    first_pattern_input.totalAngle = adsk.core.ValueInput.createByString('360 deg')
    first_pattern_input.isSymmetric = False  # Set to False if not symmetric
    first_pattern = circular_patterns.add(first_pattern_input)

def create_tube(t_mm, height_mm, raio_interno, distance_first_cut, distance_second_cut, circle_diameter_mm, qty_first_cut, qty_second_cut):
    app = adsk.core.Application.get()
    ui = app.userInterface
    design = app.activeProduct

    # Get the root component of the active design.
    root_comp = design.rootComponent

    # Create a new sketch on the XY plane.
    sketches = root_comp.sketches
    xy_plane = root_comp.xYConstructionPlane
    sketch = sketches.add(xy_plane)

    # Draw the square geometry.
    lines = sketch.sketchCurves.sketchLines
    start_point = adsk.core.Point3D.create(raio_interno, 0, 0)
    end_point1 = adsk.core.Point3D.create((t_mm/10) + raio_interno, 0, 0)
    end_point2 = adsk.core.Point3D.create((t_mm/10) + raio_interno, height_mm, 0)
    end_point3 = adsk.core.Point3D.create(raio_interno, height_mm, 0)

    lines.addByTwoPoints(start_point, end_point1)
    lines.addByTwoPoints(end_point1, end_point2)
    lines.addByTwoPoints(end_point2, end_point3)
    lines.addByTwoPoints(end_point3, start_point)

    # Finish the sketch.
    sketch.isComputeDeferred = False

    # Create the revolve feature.
    revolves = root_comp.features.revolveFeatures
    height_line = lines.item(2)  # Assuming the height line is the third line created.
    rev_input = revolves.createInput(sketch.profiles.item(0), root_comp.yConstructionAxis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    rev_input.setAngleExtent(True, adsk.core.ValueInput.createByReal(2 * math.pi))
    rev = revolves.add(rev_input)

    # Calculate the offset for the construction plane in mm.
    offset_value_mm = ((raio_interno*10) + t_mm) 

    # Create a plane parallel to the YZ plane with the calculated offset.
    planes = root_comp.constructionPlanes
    yz_plane_input = planes.createInput()
    yz_plane_input.setByOffset(root_comp.yZConstructionPlane, adsk.core.ValueInput.createByString(f'{offset_value_mm} mm'))
    yz_plane = planes.add(yz_plane_input)

    # Create a circle with a diameter defined by the user on the displaced plane.
    circle_radius_mm = circle_diameter_mm / 2  # Radius is half the diameter

    # Create the first circle for the first hole.
    first_circle_center = adsk.core.Point3D.create(0, distance_first_cut, 0)  # Fixed position in X and Z axes, defined position in Y axis
    first_circle_sketch = sketches.add(yz_plane)
    first_circle = first_circle_sketch.sketchCurves.sketchCircles.addByCenterRadius(first_circle_center, circle_radius_mm)
    first_circle_profile = first_circle_sketch.profiles.item(0)
   
    # Extrude cut the first circle with a depth equal to raio_interno.
    depth_hole = -t_mm*2
    extrudes = root_comp.features.extrudeFeatures
    ext_input = extrudes.createInput(first_circle_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
    distance_input = adsk.core.ValueInput.createByString(f'{depth_hole} mm')
    ext_input.setDistanceExtent(False, distance_input)
    first_cut = extrudes.add(ext_input)

    # Create the second circle for the second hole.
    second_circle_center = adsk.core.Point3D.create(0, distance_second_cut, 0)  # Fixed position in X and Z axes, defined position in Y axis
    second_circle_sketch = sketches.add(yz_plane)
    second_circle = second_circle_sketch.sketchCurves.sketchCircles.addByCenterRadius(second_circle_center, circle_radius_mm)
    second_circle_profile = second_circle_sketch.profiles.item(0)

    # Extrude cut the second circle with a depth equal to raio_interno.
    ext_input = extrudes.createInput(second_circle_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
    ext_input.setDistanceExtent(False, distance_input)
    second_cut = extrudes.add(ext_input)

    # Circular patterns
    circular_patterns = root_comp.features.circularPatternFeatures

    # Create a collection for the first cut features.
    first_cut_features_collection = adsk.core.ObjectCollection.create()
    first_cut_features_collection.add(first_cut)

    # Create a collection for the second cut features.
    second_cut_features_collection = adsk.core.ObjectCollection.create()
    second_cut_features_collection.add(second_cut)

    # Create the circular pattern for the cut features.
    first_pattern_input = circular_patterns.createInput(first_cut_features_collection, root_comp.yConstructionAxis)
    first_pattern_input.quantity = adsk.core.ValueInput.createByString(str(qty_first_cut))
    first_pattern_input.totalAngle = adsk.core.ValueInput.createByString('360 deg')
    first_pattern_input.isSymmetric = False  # Set to False if not symmetric
    first_pattern = circular_patterns.add(first_pattern_input)

    # Create the circular pattern for the cut features.
    second_pattern_input = circular_patterns.createInput(second_cut_features_collection, root_comp.yConstructionAxis)
    second_pattern_input.quantity = adsk.core.ValueInput.createByString(str(qty_second_cut))
    second_pattern_input.totalAngle = adsk.core.ValueInput.createByString('360 deg')
    second_pattern_input.isSymmetric = False  # Set to False if not symmetric
    second_pattern = circular_patterns.add(second_pattern_input)

def create_bulkhead(distance_second_cut, qty_second_cut, raio_interno, radius_nozzle, width_diverg, height_converg, inner_diameter, distance_first_cut, circle_diameter_mm, qty_first_cut, height_mm, t_mm):
    app = adsk.core.Application.get()
    ui = app.userInterface
    design = app.activeProduct

    # Get the root component of the active design.
    root_comp = design.rootComponent

    # Create a new sketch on the XY plane.
    sketches = root_comp.sketches
    xz_plane = root_comp.xZConstructionPlane
    sketch = sketches.add(xz_plane)

    # Draw the square geometry.
    lines = sketch.sketchCurves.sketchLines
    start_point = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut+1.5*circle_diameter_mm))
    end_point1 = adsk.core.Point3D.create(raio_interno-1.5, 0, (distance_second_cut+1.5*circle_diameter_mm))
    end_point2 = adsk.core.Point3D.create(raio_interno-1.5, 0, (distance_second_cut-4*circle_diameter_mm+1))
    end_point3 = adsk.core.Point3D.create(0, 0, (distance_second_cut-4*circle_diameter_mm+1))
    end_point4 = adsk.core.Point3D.create(0, 0, (distance_second_cut-4.5*circle_diameter_mm))
    end_point5 = adsk.core.Point3D.create(raio_interno-0.3, 0, (distance_second_cut-4.5*circle_diameter_mm))
    end_point6 = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut-4.5*circle_diameter_mm+0.3))
    end_point7 = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut-4*circle_diameter_mm+0.3))
    end_point8 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, (distance_second_cut-4*circle_diameter_mm+0.3))
    end_point9 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, (distance_second_cut-3*circle_diameter_mm+0.3))
    end_point10 = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut-3*circle_diameter_mm+0.3))
    end_point11 = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut-2.5*circle_diameter_mm+0.3))
    end_point12 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, (distance_second_cut-2.5*circle_diameter_mm+0.3))
    end_point13 = adsk.core.Point3D.create(raio_interno-circle_diameter_mm, 0, (distance_second_cut-1.5*circle_diameter_mm+0.3))
    end_point14 = adsk.core.Point3D.create(raio_interno-0.05, 0, (distance_second_cut-1.5*circle_diameter_mm+0.3))

    line1 = lines.addByTwoPoints(start_point, end_point1)
    line2 = lines.addByTwoPoints(end_point1, end_point2)
    line3 = lines.addByTwoPoints(end_point2, end_point3)
    line4 = lines.addByTwoPoints(end_point3, end_point4)
    line5 = lines.addByTwoPoints(end_point4, end_point5)
    line6 = lines.addByTwoPoints(end_point5, end_point6)
    line7 = lines.addByTwoPoints(end_point6, end_point7)
    line8 = lines.addByTwoPoints(end_point7, end_point8)
    line9 = lines.addByTwoPoints(end_point8, end_point9)
    line10 = lines.addByTwoPoints(end_point9, end_point10)
    line11 = lines.addByTwoPoints(end_point10, end_point11)
    line12 = lines.addByTwoPoints(end_point11, end_point12)
    line13 = lines.addByTwoPoints(end_point12, end_point13)
    line14 = lines.addByTwoPoints(end_point13, end_point14)
    line15 = lines.addByTwoPoints(end_point14, start_point)

     # Add a fillet at end_point3 with a radius of 5mm.
    sketch.sketchCurves.sketchArcs.addFillet(line2, end_point2, line3, end_point2, 0.5)
    sketch.sketchCurves.sketchArcs.addFillet(line11, end_point11, line12, end_point11, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line13, end_point13, line14, end_point13, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line12, end_point12, line13, end_point12, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line14, end_point14, line15, end_point14, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line7, end_point7, line8, end_point7, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line8, end_point8, line9, end_point8, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line9, end_point9, line10, end_point9, circle_diameter_mm/10)
    sketch.sketchCurves.sketchArcs.addFillet(line10, end_point10, line11, end_point10, circle_diameter_mm/10)

    # Finish the sketch.
    sketch.isComputeDeferred = False

    # Create the revolve feature.
    revolves = root_comp.features.revolveFeatures
    height_line = lines.item(2)  # Assuming the height line is the third line created.
    rev_input = revolves.createInput(sketch.profiles.item(0), root_comp.yConstructionAxis, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
    rev_input.setAngleExtent(True, adsk.core.ValueInput.createByReal(2 * math.pi))
    rev = revolves.add(rev_input)

    # Calculate the offset for the construction plane in mm.
    offset_value_mm = (raio_interno) * 10

    # Create a plane parallel to the YZ plane with the calculated offset.
    planes = root_comp.constructionPlanes
    yz_plane_input = planes.createInput()
    yz_plane_input.setByOffset(root_comp.yZConstructionPlane, adsk.core.ValueInput.createByString(f'{offset_value_mm} mm'))
    yz_plane = planes.add(yz_plane_input)

    # Create a circle with a diameter defined by the user on the displaced plane.
    circle_radius_mm = circle_diameter_mm / 2  # Radius is half the diameter

     # Create the second circle for the second hole.
    second_circle_center = adsk.core.Point3D.create(0, distance_second_cut, 0)  # Fixed position in X and Z axes, defined position in Y axis
    second_circle_sketch = sketches.add(yz_plane)
    second_circle = second_circle_sketch.sketchCurves.sketchCircles.addByCenterRadius(second_circle_center, circle_radius_mm)
    second_circle_profile = second_circle_sketch.profiles.item(0)

    # Extrude cut the second circle with a depth equal to raio_interno.
    depth_hole = -t_mm-100
    extrudes = root_comp.features.extrudeFeatures
    ext_input = extrudes.createInput(second_circle_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
    distance_input = adsk.core.ValueInput.createByString(f'{depth_hole} mm')
    ext_input.setDistanceExtent(False, distance_input)
    second_cut = extrudes.add(ext_input)

    # Circular patterns
    circular_patterns = root_comp.features.circularPatternFeatures




  # Create a collection for the second cut features.
    second_cut_features_collection = adsk.core.ObjectCollection.create()
    second_cut_features_collection.add(second_cut)




 # Create the circular pattern for the cut features.
    second_pattern_input = circular_patterns.createInput(second_cut_features_collection, root_comp.yConstructionAxis)
    second_pattern_input.quantity = adsk.core.ValueInput.createByString(str(qty_second_cut))
    second_pattern_input.totalAngle = adsk.core.ValueInput.createByString('360 deg')
    second_pattern_input.isSymmetric = False  # Set to False if not symmetric
    second_pattern = circular_patterns.add(second_pattern_input)

def create_grain(raio_interno_input, distance_first_cut, circle_diameter_mm, radius_nozzle, hole_radius, num_cylinders=1, distance_between_faces=2):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent

        # Calcular o comprimento do cilindro
        cylinder_length = 0.5 * (6 * (raio_interno_input - 0.1) + (radius_nozzle * 2 + 0.1))

        # Calcular o deslocamento no eixo Z
        z_offset = distance_first_cut + 4 * circle_diameter_mm + 0.6

        # Criação de um esboço no plano XZ
        sketches = rootComp.sketches
        xzPlane = rootComp.xZConstructionPlane
        sketch = sketches.add(xzPlane)

        # Criando o círculo externo (do tubo)
        center_point = adsk.core.Point3D.create(0, 0, z_offset)
        circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(center_point, (raio_interno_input - 0.1))

        # Criando o círculo para o furo no centro do cilindro
        #hole_radius = radius_nozzle + 0.1  # Aumenta 0.1 mm no diâmetro do furo
        hole_circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(center_point, (hole_radius/10))

        # Criando o perfil para extrusão
        profiles = adsk.core.ObjectCollection.create()
        profiles.add(sketch.profiles.item(0))  # Perfil do tubo

        # Criando a extrusão do tubo com o comprimento calculado
        extrudes = rootComp.features.extrudeFeatures
        distance = adsk.core.ValueInput.createByReal(cylinder_length)  # Usando o comprimento calculado
        extrude_input = extrudes.createInput(profiles, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        extrude_input.setDistanceExtent(False, distance)
        extrude = extrudes.add(extrude_input)

        # Criando o furo no centro do cilindro
        hole_profile = adsk.core.ObjectCollection.create()
        hole_profile.add(sketch.profiles.item(1))  # Perfil do furo

        # Realizando o corte com o perfil do furo
        cut_input = extrudes.createInput(hole_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
        cut_input.setDistanceExtent(True, adsk.core.ValueInput.createByReal(-cylinder_length))  # Corte completo através do cilindro

        # Agora, vamos criar o padrão linear de cilindros
        for i in range(1, num_cylinders):
            # Calculando o deslocamento no eixo Z para o próximo cilindro
            new_z_offset = z_offset + i * (distance_between_faces+(cylinder_length))

            # Criando o esboço para o novo cilindro
            center_point = adsk.core.Point3D.create(0, 0, new_z_offset)
            sketch = sketches.add(xzPlane)

            # Criando o círculo externo (do tubo) para o novo cilindro
            circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(center_point, (raio_interno_input - 0.1))

            # Criando o círculo para o furo no centro do cilindro
            hole_circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(center_point, (hole_radius/10))

            # Criando o perfil para extrusão do novo cilindro
            profiles = adsk.core.ObjectCollection.create()
            profiles.add(sketch.profiles.item(0))  # Perfil do tubo

            # Criando a extrusão do novo cilindro
            extrude_input = extrudes.createInput(profiles, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
            extrude_input.setDistanceExtent(False, distance)
            extrude = extrudes.add(extrude_input)

            # Criando o furo no centro do novo cilindro
            hole_profile = adsk.core.ObjectCollection.create()
            hole_profile.add(sketch.profiles.item(1))  # Perfil do furo

            # Realizando o corte com o perfil do furo
            cut_input = extrudes.createInput(hole_profile, adsk.fusion.FeatureOperations.CutFeatureOperation)
            cut_input.setDistanceExtent(True, adsk.core.ValueInput.createByReal(-cylinder_length))  # Corte completo através do cilindro

    except Exception as e:
        if ui:
            ui.messageBox(f"Erro ao criar grãos:\n{traceback.format_exc()}")
           
import math
import adsk.core
import traceback

# Constantes fornecidas
To = 1710  # K (temperatura ideal de combustão)
M = 42.39  # kg/kmol (massa molar dos produtos)
y = 1.131  # Razão entre capacidades caloríficas (Cp/Cv)
alpha = 1000000  # Fator de conversão (MPa para Pa)
rho = 0.00000188  # Densidade do propelente real em kg/mm³
Pa = 101325  # Pa (pressão atmosférica)
R_universal = 8314  # J/kmol-K (constante universal dos gases)
R = 196.1  # J/kg-K (constante específica dos gases)

def calcular_m_ponto(area_total, r, rho):
    """
    Calcula o fluxo ṁ com base na área de queima, taxa de queima e densidade do propelente.


    Parâmetros:
    - Ab (float): Área de queima (m²)
    - r (float): Taxa de queima (m/s)
    - rho (float): Densidade do propelente (kg/m³)


    Retorna:
    - m_ponto (float): Fluxo ṁ (kg/s)
    """
    return area_total * r * rho

def calcular_mach(width_diverg, area_nozzle, y, ui):
    # Cálculo da área divergente Ad
    Ad = math.pi * width_diverg**2

    # Definir a equação para resolver numericamente
    def equation(mach):
        # Verificar se y é igual a 1
        if y == 1:
            ui.messageBox("Erro: y não pode ser igual a 1, pois isso causaria uma divisão por zero.")
            return float('inf')  # Retorna um valor infinito para indicar erro

        # Caso y não seja igual a 1, podemos prosseguir com a equação
        return (1 / mach**2) * ((2 / (y + 1)) * (1 + (y - 1) / 2 * mach**2))**((y + 1) / (y - 1)) - (Ad / area_nozzle)**2

    # Método da bisseção
    def bisection_method(a, b, tol=1e-5, max_iter=100):
        fa = equation(a)
        fb = equation(b)

        # Verificar se os valores nas extremidades do intervalo têm sinais opostos
        if fa * fb >= 0:
            ui.messageBox("Erro: O intervalo inicial não contém uma raiz. Tente ajustar o intervalo.")
            return None

        # Método da bisseção
        for i in range(max_iter):
            c = (a + b) / 2
            fc = equation(c)
            if abs(fc) < tol:
                return c
            elif fc * fa < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

        ui.messageBox("Erro: Número máximo de iterações alcançado.")
        return None

    # Intervalo ajustado para a raiz maior (maior que 1)
    a2, b2 = 1.0, 5.0  # Intervalo para a segunda raiz (maior que 1)

    # Buscar a raiz maior
    mach_solution_2 = bisection_method(a2, b2)
    
    return mach_solution_2

def calcular_ve(mach):
    return mach * 343

def calcular_pe(mach, Po):
    pressao_relativa = (1 + (y - 1) / 2 * mach**2)**(-y / (y - 1))  # Razão p/Po
    return Po * pressao_relativa  # Multiplica Po pela razão para obter p

def calcular_empuxo(m_ponto, Ve, Pe, Pa, area_nozzle):
    """
    Calcula o empuxo separando os fatores para verificação.
    Parâmetros:
    - m_ponto (float): Fluxo de massa (kg/s)
    - Ve (float): Velocidade de saída (m/s)
    - Pe (float): Pressão de saída (Pa)
    - Pa (float): Pressão ambiente (Pa)
    - area_nozzle (float): Área do nozzle (m²)

    Retorna:
    - F (float): Empuxo (N)
    """
    # Garantir que todas as variáveis sejam do tipo float
    try:
        m_ponto = float(m_ponto)
        Ve = float(Ve)
        Pe = float(Pe)
        Pa = float(Pa)
        area_nozzle = float(area_nozzle)
    except ValueError as e:
        app = adsk.core.Application.get()
        ui = app.userInterface
        ui.messageBox(f"Erro ao converter variáveis para tipo numérico: {str(e)}")
        return None

    # Fator 1: Contribuição do fluxo de massa e velocidade de saída
    fator1 = m_ponto * Ve

    # Fator 2: Contribuição da pressão (diferença entre Pe e Pa) e área do nozzle
    fator2 = (Pe - Pa) * area_nozzle / 1e3

    # Imprimir os fatores na interface do Fusion 360
    app = adsk.core.Application.get()
    ui = app.userInterface

    # Calcular o empuxo total
    F = fator1 + fator2
    return F

import adsk.core, adsk.fusion, adsk.cam

def calcular_taxa_queima(Po):
    """
    Calcula a taxa de queima com base na pressão Po.
    
    Parâmetros:
    - Po (float): Pressão (MPa)
    
    Retorna:
    - r (float): Taxa de queima (mm/s) se dentro do intervalo permitido.
    """
    app = adsk.core.Application.get()
    ui = app.userInterface
    
    if Po < 0.103:
        ui.messageBox("Pressão fora do intervalo permitido, diminua o diâmetro da garganta.")
        return None
    elif Po > 11.2:
        ui.messageBox("Pressão fora do intervalo permitido, aumente o diâmetro da garganta.")
        return None
    
    if 0.103 <= Po < 0.779:
        a, n = 8.88, 0.619
    elif 0.779 <= Po < 2.57:
        a, n = 7.55, -0.009
    elif 2.57 <= Po < 5.93:
        a, n = 3.84, 0.688
    elif 5.93 <= Po < 8.5:
        a, n = 17.2, -0.148
    elif 8.2 <= Po <= 11.2:
        a, n = 4.78, 0.442
    
    return a * (Po ** n)



def calcular_area_total(raio_interno, hole_radius, cylinder_length, num_cylinders):
    """
    Calcula a área total de queima com base nas dimensões fornecidas.
    Parâmetros:
    - raio_interno_input (float): Distância da origem (mm)
    - hole_radius (float): Raio do furo (mm)
    - cylinder_length (float): Comprimento do cilindro (mm)
    - num_cylinders (int): Número de cilindros
    Retorna:
    - area_total (float): Área total de queima (m²)
    """
    r_tubo = (raio_interno)*10
    area_faces_planas = (math.pi * (r_tubo ** 2)) - (math.pi * (hole_radius ** 2))
    area_furo = 2 * math.pi * hole_radius * cylinder_length * 10  # Multiplicando por 10 como no código original
    return num_cylinders * ((2 * area_faces_planas) + area_furo)

def calcular_area_nozzle(radius_nozzle):

    # Calcula a área do nozzle com base no raio fornecido.
    # Parâmetros:
    # - radius_nozzle (float): Raio do nozzle (cm)
    # Retorna:
    # - area_nozzle (float): Área do nozzle (m²)

    return math.pi * ((radius_nozzle * 10) ** 2)

def calcular_pressao(P1, rho, R, To, area_total, area_nozzle):
    # Inicializando a pressão inicial em MPa (6 MPa como hipótese)
    gamma = 1.13
    P1_atual = 6 * 1_000_000  # Convertendo para Pa
    tolerancia = 0.2 * 1_000_000  # 0.2 MPa em Pa (tolerância para a diferença de pressão)
    diferenca_pressao = float('inf')  # Definindo uma diferença inicial grande
    iteracao = 0

    # Imprimir o valor de P1 para verificação na interface do Fusion 360
    app = adsk.core.Application.get()
    ui = app.userInterface

    while diferenca_pressao >= tolerancia:
        iteracao += 1

        # Imprimir as variáveis r_tubo e hole_radius

        # Calcular r com a pressão atual
        try:
            r = calcular_taxa_queima(P1_atual / 1_000_000)  # Passando P1 em MPa para a função
            if r < 0:
                ui.messageBox(f"Erro: taxa de queima (r) negativa na iteração {iteracao}")
                return None
        except ValueError as e:
            ui.messageBox(f"Erro ao calcular a taxa de queima: {str(e)}")
            return None


        # Calcular Po com o valor de r
        Po_novo = 10000*area_total*r*rho*((gamma*R*To)**(1/2))/(area_nozzle*gamma*(((2/(gamma+1))**((gamma+1)/(gamma-1)))**(1/2)))

        # Verificar se Po não está negativo
        if Po_novo < 0:
            ui.messageBox(f"Erro: Po calculado negativo na iteração {iteracao}")
            return None

        # Calcular a diferença de pressão entre a iteração anterior e a nova
        diferenca_pressao = abs(Po_novo - P1_atual)
        

        # Atualizar P1 para a próxima iteração
        P1_atual = Po_novo  # Atualiza a pressão para a próxima iteração


    # Quando a diferença for menor que a tolerância, salva o valor de Po como a pressão interna
    return Po_novo

# Modificando a função de execução para incluir o número de cilindros
def calcular_forca_parafusos(Po, inner_diameter, num_bolts):
    """
    Calcula a força atuante nos parafusos e a força individual de cada um.
   
    :param Po: Pressão interna do motor (Pa)
    :param inner_diameter: Diâmetro interno do tubo (mm)
    :param num_bolts: Número de parafusos
    :return: Força atuante nos parafusos (N), Força individual por parafuso (N)
    """
    # Convertendo o diâmetro para metros
    inner_diameter_m = inner_diameter / 100
    # Cálculo da força atuante nos parafusos
    força_total = Po * 3.1416 * (inner_diameter_m ** 2) 
    # Força individual por parafuso
    força_individual = força_total / num_bolts
    return força_individual

def calcular_tensao_furo(forca_individual, circle_diameter_mm, t_mm):
    """
    Calcula a tensão em cada furo devido à força atuante dos parafusos.
   
    :param forca_individual: Força individual de cada parafuso (N)
    :param furo_diametro: Diâmetro do furo (mm)
    :param espessura_tubo: Espessura do tubo (mm)
    :param diamentro_tubo: Diâmetro do tubo (mm)
    :return: Tensão individual (Pa)
    """
    # Convertendo para metros
    furo_diametro_m = circle_diameter_mm * 10
    espessura_tubo_m = t_mm
   
    # Área do furo e da região ao redor
    area_furo1 = (3.1416 * (furo_diametro_m ** 2)) / 4
    area_furo2 = (3.1416 * (furo_diametro_m/2) * espessura_tubo_m)
   
    # Cálculo da tensão
    tensao_individual = forca_individual / ((area_furo1 + area_furo2)/2)
    return tensao_individual

def calcular_espessura_tubo(Po, inner_diameter, yield_lim, fs):
    """
    Calcula a espessura do tubo utilizando a equação de vaso de pressão e o limite de escoamento.
    Garante que a espessura mínima seja de 2 mm.
    :param Po: Pressão interna (Pa ou N/m²)
    :param inner_diameter: Diâmetro interno do tubo (mm)
    :param yield_lim: Limite de escoamento (Pa ou N/m²)
    :param fs: Fator de segurança
    :return: Espessura do tubo (mm)
    """
    # Convertendo o diâmetro para metros
    D = inner_diameter / 10  # mm para metros
    yield_lim = float(yield_lim) * 1e6

    # Cálculo da espessura usando a fórmula de vaso de pressão
    t = (Po * D) / (2 * yield_lim * fs - Po)
    # Convertendo de volta para mm
    t_mm = t * 1000
    # Garantindo que a espessura mínima seja de 2 mm
    if t_mm < 2:
        t_mm = 2.0
    return t_mm

def calcular_massa_total_propelente(num_cylinders, area_faces_planas, cylinder_length, rho):
    """
    Calcula a massa total de propelente (MT).
    
    Parâmetros:
    - area_faces_planas (float): Área das faces planas (m²)
    - cylinder_length (float): Comprimento do cilindro (m)
    - rho (float): Densidade do propelente (kg/m³)
    
    Retorna:
    - MT (float): Massa total de propelente (kg)
    """
    volume = num_cylinders * area_faces_planas * cylinder_length * 10  # Volume do propelente (mm³)
    MT = volume * rho  # Massa total de propelente (kg)
    return MT

def calcula_forca_total(F_empuxo, massa_inicial, raio_interno, t_mm, cd, densidade_ar, TQ, delta_t, ui, it):
    """
    Calcula a força total durante e após a queima do motor, aceleração, velocidade e apogeu.
    
    Parâmetros:
        F_empuxo (float): Força de empuxo do motor (N).
        massa_inicial (float): Massa inicial do foguete (kg).
        raio_interno (float): Raio interno do foguete (m).
        t_mm (float): Espessura das paredes do foguete (mm).
        cd (float): Coeficiente de arrasto.
        densidade_ar (float): Densidade do ar (kg/m³).
        TQ (float): Tempo de queima do motor (s).
        delta_t (float): Intervalo de tempo para integração (s).
        ui: Interface do usuário para exibir mensagens.
        it: Iteração para controle de iteração (não utilizado na função atual).

    Retorna:
        forças (list): Lista contendo as forças totais durante e após a queima.
        aceleracoes (list): Lista contendo as acelerações durante e após a queima.
        velocidades (list): Lista contendo as velocidades durante e após a queima.
        altura_maxima (float): Altura máxima (apogeu) atingida pelo foguete (em metros).
    """
    g = 9.81  # Gravidade (m/s²)
    velocidade_do_som = 343  # Velocidade do som no ar a 20°C (m/s)
    
    # Condições iniciais
    tempo = 0
    massa = massa_inicial
    area_frontal = math.pi * (((raio_interno*10) + t_mm) / 1000)**2  # Convertendo mm para metros
    velocidade = 0  # Velocidade inicial (em m/s)
    altura = 0  # Altura inicial (em metros)
    altura_maxima = 0  # Para armazenar o apogeu
    
    # Variáveis para armazenar os valores máximos
    forca_maxima = 0
    aceleracao_maxima = 0
    velocidade_maxima = 0
    mach_maximo = 0

    # Durante a queima do motor
    while tempo <= TQ:
        # Peso do foguete
        peso = massa * g
        
        # Força de arrasto
        arrasto = 0.5 * cd * densidade_ar * area_frontal * max(velocidade, 0)**2
        
        # Força total (empuxo - peso - arrasto)
        forca_total = F_empuxo - peso - arrasto
        forca_maxima = max(forca_maxima, forca_total)
        
        # Cálculo da aceleração (F = ma => a = F/m)
        aceleracao = forca_total / massa
        aceleracao_maxima = max(aceleracao_maxima, aceleracao)
        
        # Cálculo da velocidade (v = v + a * delta_t)
        velocidade += aceleracao * delta_t
        velocidade_maxima = max(velocidade_maxima, velocidade)
        
        # Atualizar a altura (s = s + v * delta_t)
        altura += velocidade * delta_t
        altura_maxima = max(altura_maxima, altura)
        
        # Cálculo do número de Mach
        mach = velocidade / velocidade_do_som
        mach_maximo = max(mach_maximo, mach)
        
        tempo += delta_t

    # Após a queima do motor (empuxo = 0)
    while velocidade > 0:  # Subida até o apogeu
        # Peso do foguete
        peso = massa * g
        
        # Força de arrasto
        arrasto = 0.5 * cd * densidade_ar * area_frontal * max(velocidade, 0)**2
        
        # Força total (apenas peso e arrasto)
        forca_total = -peso - arrasto
        forca_maxima = max(forca_maxima, forca_total)
        
        # Cálculo da aceleração (F = ma => a = F/m)
        aceleracao = forca_total / massa
        aceleracao_maxima = max(aceleracao_maxima, aceleracao)
        
        # Cálculo da velocidade (v = v + a * delta_t)
        velocidade += aceleracao * delta_t
        velocidade_maxima = max(velocidade_maxima, velocidade)
        
        # Atualizar a altura (s = s + v * delta_t)
        altura += velocidade * delta_t
        altura_maxima = max(altura_maxima, altura)
        
        # Cálculo do número de Mach
        mach = velocidade / velocidade_do_som
        mach_maximo = max(mach_maximo, mach)
        
        tempo += delta_t

    # Exibindo os resultados máximos
    resultados = (
        f"Altura máxima (apogeu): {altura_maxima:.2f} m\n"
        f"Força máxima: {forca_maxima:.2f} N\n"
        f"Aceleração máxima: {aceleracao_maxima:.2f} m/s²\n"
        f"Aceleração máxima: {aceleracao_maxima / g:.2f} g\n"
        f"Velocidade máxima: {velocidade_maxima:.2f} m/s\n"
        f"Mach máximo: {mach_maximo:.2f}\n"
    )
    
    ui.messageBox(resultados, "Parâmetros da Trajetória")
    
    return forca_maxima, aceleracao_maxima, velocidade_maxima, altura_maxima

def run_script_combined():
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Entrada de dados do usuário
        raio_interno_input = ui.inputBox("Digite o diâmetro interno do tubo (em mm):", "Distância da Origem - Eixo X", "94")[0]
        radius_nozzle_input = ui.inputBox("Digite o diâmetro da seção crítica da garganta da tubeira:", "Diâmetro da garganta da tubeira", "20")[0]
        num_cylinders_input = ui.inputBox("Digite o número de grãos a serem criados:", "Número de Grãos", "4")[0]
        fs_input = ui.inputBox("Digite o fator de segurança desejado para o cálculo estrutural:", "Fator de Segurança", "2.5")[0]
        yield_lim_input = ui.inputBox("Digite a tensão limite de escoamento do tubo (em MPa):", "Tensão de Escoamento", "250")[0]  # Nova entrada para yield_lim
        massa_input = ui.inputBox("Digite a massa total do foguete (em kg):", "Massa do foguete", "15")[0]

        # Convertendo entradas para valores em mm e dividindo por 10 quando necessário
        raio_interno = float(raio_interno_input) / 20
        height_converg = (float(raio_interno) - float(radius_nozzle_input) / 10 - 0.3)  # * tan (60°)
        width_diverg = ((float(raio_interno)) * 0.86) * 2 / 3  # + (float(radius_nozzle_input)/5)
        inner_diameter = float(raio_interno)
        radius_nozzle = float(radius_nozzle_input) / 20
        num_cylinders = int(num_cylinders_input)  # Convertendo para inteiro
        yield_lim = float(yield_lim_input)
        fs = float(fs_input)
        distance_between_faces = 0.2
        massa_inicial = float(massa_input)
        hole_radius = (radius_nozzle+0.1)*10

        # Condicional para definir o diâmetro do furo
        if raio_interno < 5:
            circle_diameter_mm = 0.6
            distance_first_cut = 0.6*2
            d_second_cut = 0.6*2
        else:
            circle_diameter_mm = 0.8
            distance_first_cut = 0.8*2
            d_second_cut = 0.8*2

        # Cálculos adicionais para o comprimento do cilindro
        cylinder_length = 0.5 * (6 * (raio_interno - 0.1) + (radius_nozzle * 2 + 0.1))
        z_offset = distance_first_cut + 4 * circle_diameter_mm + 0.6
        r_tubo = (raio_interno)*10
        area_faces_planas = (math.pi * (r_tubo ** 2)) - (math.pi * (hole_radius ** 2))
        area_furo = 2 * math.pi * hole_radius * cylinder_length * 10
        kn = (num_cylinders * (2 * area_faces_planas + area_furo))/(math.pi * ((radius_nozzle * 10) ** 2))

        # Calcular a área da tubeira (nozzle)
        area_nozzle = math.pi * (radius_nozzle ** 2)
        area_total = calcular_area_total(raio_interno, hole_radius, cylinder_length, num_cylinders)

        # Calculando a pressão Po a partir da entrada P1
        P1 = 101325  # Pressão de entrada (Pa), você pode modificar isso para receber como entrada
        Po = calcular_pressao(P1, rho, R, To, area_total, area_nozzle)

        # Cálculo da espessura do tubo
        t_mm = calcular_espessura_tubo(Po, inner_diameter, yield_lim, fs)
   
        # Novo cálculo para height_mm
        height_mm = ((num_cylinders*(cylinder_length+distance_between_faces)) + z_offset + 0.1 + 4.5*circle_diameter_mm + distance_first_cut)
        distance_second_cut = (height_mm - float(d_second_cut))

        # Loop para variar num_bolts
        num_bolts = 4
        while True:
            # Chamada da função para calcular a força e tensão nos parafusos
            força_individual = calcular_forca_parafusos(Po, inner_diameter, num_bolts)
            tensao_individual = calcular_tensao_furo(força_individual, circle_diameter_mm, t_mm)

            # Calcular o fator de segurança
            fator_seguranca = yield_lim / tensao_individual

            # Atualizar as variáveis qty_first_cut e qty_second_cut com o valor de num_bolts
            qty_first_cut = num_bolts
            qty_second_cut = num_bolts

            # Verifica se o fator de segurança é maior que 2,5
            if fator_seguranca > fs or num_bolts >= 50:
                break

            # Incrementa o número de parafusos
            num_bolts += 2

        # Exibir os resultados para o número atual de parafusos
        mensagem2 = (f"\nNúmero de Parafusos: {num_bolts}\n"
                      f"Força individual por parafuso: {força_individual:.2f} N\n"
                      f"Diâmetro do furo: {circle_diameter_mm:.2f} mm\n"
                      f"Espessura: {t_mm:.2f} mm\n"
                      f"Tensão individual no furo: {tensao_individual:.2f} Pa\n"
                      f"Fator de segurança: {fator_seguranca:.2f}\n"
                      f"Espessura {t_mm} mm")
        ui.messageBox(mensagem2, "Cálculo Estrutural")

        # Chamada da função para calcular a força e tensão nos parafusos
        força_individual = calcular_forca_parafusos(Po, inner_diameter, num_bolts)
        tensao_individual = calcular_tensao_furo(força_individual, circle_diameter_mm, t_mm)

        # Fator de segurança
        fator_seguranca = yield_lim / tensao_individual

        # Chamada da função com furo no centro e comprimento calculado
        create_grain(raio_interno, distance_first_cut, circle_diameter_mm, radius_nozzle, hole_radius, num_cylinders, distance_between_faces)
        create_nozzle(raio_interno, radius_nozzle, width_diverg, height_converg, inner_diameter, distance_first_cut, circle_diameter_mm, qty_first_cut, t_mm)
        create_tube(t_mm, height_mm, raio_interno, distance_first_cut, distance_second_cut, circle_diameter_mm, qty_first_cut, qty_second_cut)
        create_bulkhead(distance_second_cut, qty_second_cut, raio_interno, radius_nozzle, width_diverg, height_converg, inner_diameter, distance_first_cut, circle_diameter_mm, qty_first_cut, height_mm, t_mm)

        # Calcular a área das faces planas e furos
        Pa = 101325
        # run_area_calculation(raio_interno, hole_radius, cylinder_length, num_cylinders, radius_nozzle, rho, y, R, To, R_universal, M, Pa, R, area_faces_planas, r_tubo)

         # Calcular o valor de Mach
        mach = calcular_mach(width_diverg, area_nozzle, y, ui)

        # Calcular a velocidade correspondente
        Ve = calcular_ve(mach)

        # Calcular a pressão estática
        Pe = calcular_pe(mach, Po)

        # Calcular a taxa de queima
        r = calcular_taxa_queima(Po / 1_000_000)
        if r is None:
            ui.messageBox("Erro ao calcular a taxa de queima.")
            return

        cylinder_length2 = cylinder_length * 10

        # Calcular o fluxo de massa
        m_ponto = calcular_m_ponto(area_total, r, rho)
        if m_ponto is None:
            ui.messageBox("Erro ao calcular o fluxo de massa.")
            return
        
        # Definir pressão ambiente (Pa)
        Pa = 101325  # Exemplo: pressão ao nível do mar em Pascal

        # Calcular o empuxo
        F_empuxo = calcular_empuxo(m_ponto, Ve, Pe, Pa, area_nozzle)

        # Calcular a massa total de propelente
        MT = calcular_massa_total_propelente(num_cylinders, area_faces_planas, cylinder_length, rho)

        # Calcular o tempo de queima
        TQ = MT/m_ponto

        # Calcular o impulso total
        it = F_empuxo*TQ

                # Exibir os resultados na barra de eventos
        mensagem = (
            f"O valor de Mach na saída da tubeira (M) é: {mach:.4f}\n"
            f"A velocidade dos gases na saída da tubeira é: {Ve:.2f} m/s\n"
            f"A pressão no interior da câmara de combustão é: {Po:.2f} Pa\n"
            f"A pressão na saída da tubeira é: {Pe:.2f} Pa\n"
            f"Comprimento do grão: {cylinder_length2:.2f} mm\n"
            f"Fluxo de massa (m_ponto): {m_ponto:.2f} kg/s\n"
            f"Massa total de propelente: {MT:.2f} kg\n"
            f"Tempo de queima: {TQ:.2f} s\n"
            f"Empuxo: {F_empuxo:.2f} N\n"
            f"Impulso total: {it:.2f} Ns"
        )
        ui.messageBox(mensagem, "Parâmetros de Desempenho do Motor")

        # Cálculo do apogeu
        cd = 0.6  # Coeficiente de arrasto
        densidade_ar = 1.225  # kg/m³
        delta_t = 0.01  # Passo de integração (s)

        forças = calcula_forca_total(F_empuxo, massa_inicial, raio_interno, t_mm, cd, densidade_ar, TQ, delta_t, ui, it)

    except Exception as e:
        if ui:
            ui.messageBox('Erro:\n{}'.format(traceback.format_exc()))

# Run the combined script.
run_script_combined()

